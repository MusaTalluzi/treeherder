from treeherder.etl import buildbot
import pytest

slow = pytest.mark.slow

buildernames = [
 ('Android 2.2 Armv6 mozilla-inbound build',
  {'build_type': 'opt',
   'job_type': 'build',
   'platform': {'arch': 'armv6',
                'os': 'android',
                'os_platform': 'android-2-2-armv6',
                'vm': False}}),

 ('Android 2.2 Armv6 Tegra mozilla-inbound opt test crashtest',
  {'build_type': 'opt',
   'job_type': 'unittest',
   'platform': {'arch': 'armv6',
                'os': 'android',
                'os_platform': 'android-2-2-armv6',
                'vm': False}}),

 ('Android 2.2 Armv6 Tegra mozilla-inbound opt test jsreftest-1',
  {'build_type': 'opt',
   'job_type': 'unittest',
   'platform': {'arch': 'armv6',
                'os': 'android',
                'os_platform': 'android-2-2-armv6',
                'vm': False}}),

 ('Android 2.2 Armv6 Tegra mozilla-inbound opt test mochitest-1',
  {'build_type': 'opt',
   'job_type': 'unittest',
   'platform': {'arch': 'armv6',
                'os': 'android',
                'os_platform': 'android-2-2-armv6',
                'vm': False}}),

 ('Android 2.2 Armv6 Tegra mozilla-inbound opt test plain-reftest-1',
  {'build_type': 'opt',
   'job_type': 'unittest',
   'platform': {'arch': 'armv6',
                'os': 'android',
                'os_platform': 'android-2-2-armv6',
                'vm': False}}),

 ('Android 2.2 Armv6 Tegra mozilla-inbound opt test robocop-1',
  {'build_type': 'opt',
   'job_type': 'unittest',
   'platform': {'arch': 'armv6',
                'os': 'android',
                'os_platform': 'android-2-2-armv6',
                'vm': False}}),

 ('Android 2.2 Armv6 Tegra mozilla-inbound opt test xpcshell',
  {'build_type': 'opt',
   'job_type': 'unittest',
   'platform': {'arch': 'armv6',
                'os': 'android',
                'os_platform': 'android-2-2-armv6',
                'vm': False}}),

 ('Android 2.2 Debug mozilla-inbound build',
  {'build_type': 'debug',
   'job_type': 'build',
   'platform': {'arch': 'x86',
                'os': 'android',
                'os_platform': 'android-2-2',
                'vm': False}}),

 ('Android 2.2 mozilla-inbound build',
  {'build_type': 'opt',
   'job_type': 'build',
   'platform': {'arch': 'x86',
                'os': 'android',
                'os_platform': 'android-2-2',
                'vm': False}}),

 ('Android 2.2 Tegra mozilla-inbound opt test crashtest',
  {'build_type': 'opt',
   'job_type': 'unittest',
   'platform': {'arch': 'x86',
                'os': 'android',
                'os_platform': 'android-2-2',
                'vm': False}}),

 ('Android 2.2 Tegra mozilla-inbound talos remote-tcanvasmark',
  {'build_type': 'opt',
   'job_type': 'talos',
   'platform': {'arch': 'x86',
                'os': 'android',
                'os_platform': 'android-2-2',
                'vm': False}}),

 ('Android 4.0 Panda mozilla-inbound talos remote-tsvgx',
  {'build_type': 'opt',
   'job_type': 'talos',
   'platform': {'arch': 'x86',
                'os': 'android',
                'os_platform': 'android-4-0',
                'vm': False}}),

 ('Android 4.2 x86 mozilla-inbound build',
  {'build_type': 'opt',
   'job_type': 'build',
   'platform': {'arch': 'x86',
                'os': 'android',
                'os_platform': 'android-4-2-x86',
                'vm': False}}),

 ('b2g_emulator mozilla-inbound opt test reftest-1',
  {'build_type': 'opt',
   'job_type': 'unittest',
   'platform': {'arch': 'x86',
                'os': 'b2g',
                'os_platform': 'b2g-emu-ics',
                'vm': False}}),

 ('b2g_mozilla-inbound_emulator_dep',
  {'build_type': 'opt',
   'job_type': 'build',
   'platform': {'arch': 'x86',
                'os': 'b2g',
                'os_platform': 'b2g-emu-ics',
                'vm': False}}),

 ('b2g_mozilla-inbound_emulator-debug_dep',
  {'build_type': 'debug',
   'job_type': 'build',
   'platform': {'arch': 'x86',
                'os': 'b2g',
                'os_platform': 'b2g-emu-ics',
                'vm': False}}),

 ('b2g_mozilla-inbound_emulator-jb_dep',
  {'build_type': 'opt',
   'job_type': 'build',
   'platform': {'arch': 'x86',
                'os': 'b2g',
                'os_platform': 'b2g-emu-jb',
                'vm': False}}),

 ('b2g_mozilla-inbound_emulator-jb-debug_dep',
  {'build_type': 'debug',
   'job_type': 'build',
   'platform': {'arch': 'x86',
                'os': 'b2g',
                'os_platform': 'b2g-emu-jb',
                'vm': False}}),

 ('b2g_mozilla-inbound_linux32_gecko build',
  {'build_type': 'opt',
   'job_type': 'build',
   'platform': {'arch': 'x86',
                'os': 'linux',
                'os_platform': 'b2g-linux32',
                'vm': False}}),

 ('b2g_mozilla-inbound_linux64_gecko build',
  {'build_type': 'opt',
   'job_type': 'build',
   'platform': {'arch': 'x86_64',
                'os': 'linux',
                'os_platform': 'b2g-linux64',
                'vm': False}}),

 ('b2g_mozilla-inbound_macosx64_gecko build',
  {'build_type': 'opt',
   'job_type': 'build',
   'platform': {'arch': 'x86_64',
                'os': 'mac',
                'os_platform': 'b2g-osx',
                'vm': False}}),

 ('b2g_mozilla-inbound_unagi_dep',
  {'build_type': 'opt',
   'job_type': 'build',
   'platform': {'arch': 'x86',
                'os': 'b2g',
                'os_platform': 'b2g-device-image',
                'vm': False}}),

 ('b2g_mozilla-inbound_win32_gecko build',
  {'build_type': 'opt',
   'job_type': 'build',
   'platform': {'arch': 'x86',
                'os': 'win',
                'os_platform': 'b2g-win32',
                'vm': False}}),

 ('b2g_ubuntu64_vm mozilla-inbound opt test gaia-ui-test',
  {'build_type': 'opt',
   'job_type': 'unittest',
   'platform': {'arch': 'x86_64',
                'os': 'linux',
                'os_platform': 'b2g-linux64',
                'vm': True}}),

 ('b2g_ubuntu64_vm mozilla-inbound opt test gaia-unit',
  {'build_type': 'opt',
   'job_type': 'unittest',
   'platform': {'arch': 'x86_64',
                'os': 'linux',
                'os_platform': 'b2g-linux64',
                'vm': True}}),

 ('b2g_ubuntu64_vm mozilla-inbound opt test mochitest-1',
  {'build_type': 'opt',
   'job_type': 'unittest',
   'platform': {'arch': 'x86_64',
                'os': 'linux',
                'os_platform': 'b2g-linux64',
                'vm': True}}),

 ('Linux mozilla-inbound build',
  {'build_type': 'opt',
   'job_type': 'build',
   'platform': {'arch': 'x86',
                'os': 'linux',
                'os_platform': 'linux32',
                'vm': False}}),

 ('Linux mozilla-inbound leak test build',
  {'build_type': 'debug',
   'job_type': 'build',
   'platform': {'arch': 'x86',
                'os': 'linux',
                'os_platform': 'linux32',
                'vm': False}}),

 ('Linux mozilla-inbound leak test spidermonkey_info-warnaserrdebug build',
  {'build_type': 'debug',
   'job_type': 'build',
   'platform': {'arch': 'x86',
                'os': 'linux',
                'os_platform': 'linux32',
                'vm': False}}),

 ('Linux mozilla-inbound pgo-build',
  {'build_type': 'pgo',
   'job_type': 'build',
   'platform': {'arch': 'x86',
                'os': 'linux',
                'os_platform': 'linux32',
                'vm': False}}),

 ('Linux mozilla-inbound spidermonkey_info-warnaserr build',
  {'build_type': 'opt',
   'job_type': 'build',
   'platform': {'arch': 'x86',
                'os': 'linux',
                'os_platform': 'linux32',
                'vm': False}}),

 ('Linux x86-64 mozilla-inbound asan build',
  {'build_type': 'asan',
   'job_type': 'build',
   'platform': {'arch': 'x86_64',
                'os': 'linux',
                'os_platform': 'linux64',
                'vm': False}}),

 ('Linux x86-64 mozilla-inbound build',
  {'build_type': 'opt',
   'job_type': 'build',
   'platform': {'arch': 'x86_64',
                'os': 'linux',
                'os_platform': 'linux64',
                'vm': False}}),

 ('Linux x86-64 mozilla-inbound debug asan build',
  {'build_type': 'asan',
   'job_type': 'build',
   'platform': {'arch': 'x86_64',
                'os': 'linux',
                'os_platform': 'linux64',
                'vm': False}}),

 ('Linux x86-64 mozilla-inbound debug static analysis build',
  {'build_type': 'debug',
   'job_type': 'build',
   'platform': {'arch': 'x86_64',
                'os': 'linux',
                'os_platform': 'linux64',
                'vm': False}}),

 ('Linux x86-64 mozilla-inbound leak test build',
  {'build_type': 'debug',
   'job_type': 'build',
   'platform': {'arch': 'x86_64',
                'os': 'linux',
                'os_platform': 'linux64',
                'vm': False}}),

 ('Linux x86-64 mozilla-inbound leak test spidermonkey_tier_1-rootanalysis build',
  {'build_type': 'debug',
   'job_type': 'build',
   'platform': {'arch': 'x86_64',
                'os': 'linux',
                'os_platform': 'linux64',
                'vm': False}}),

 ('Linux x86-64 mozilla-inbound pgo-build',
  {'build_type': 'pgo',
   'job_type': 'build',
   'platform': {'arch': 'x86_64',
                'os': 'linux',
                'os_platform': 'linux64',
                'vm': False}}),

 ('Linux x86-64 mozilla-inbound spidermonkey_info-warnaserr build',
  {'build_type': 'opt',
   'job_type': 'build',
   'platform': {'arch': 'x86_64',
                'os': 'linux',
                'os_platform': 'linux64',
                'vm': False}}),

 ('OS X 10.7 64-bit mozilla-inbound leak test build',
  {'build_type': 'debug',
   'job_type': 'build',
   'platform': {'arch': 'x86_64',
                'os': 'mac',
                'os_platform': 'osx-10-7',
                'vm': False}}),

 ('OS X 10.7 mozilla-inbound build',
  {'build_type': 'opt',
   'job_type': 'build',
   'platform': {'arch': 'x86_64',
                'os': 'mac',
                'os_platform': 'osx-10-7',
                'vm': False}}),

 ('Rev3 Fedora 12 mozilla-inbound debug test mochitest-browser-chrome',
  {'build_type': 'debug',
   'job_type': 'unittest',
   'platform': {'arch': 'x86',
                'os': 'linux',
                'os_platform': 'linux32',
                'vm': False}}),

 ('Rev3 Fedora 12x64 mozilla-inbound debug test mochitest-browser-chrome',
  {'build_type': 'debug',
   'job_type': 'unittest',
   'platform': {'arch': 'x86_64',
                'os': 'linux',
                'os_platform': 'linux64',
                'vm': False}}),

 ('Rev4 MacOSX Lion 10.7 mozilla-inbound debug test jetpack',
  {'build_type': 'debug',
   'job_type': 'unittest',
   'platform': {'arch': 'x86_64',
                'os': 'mac',
                'os_platform': 'osx-10-7',
                'vm': False}}),

 ('Rev4 MacOSX Lion 10.7 mozilla-inbound debug test marionette',
  {'build_type': 'debug',
   'job_type': 'unittest',
   'platform': {'arch': 'x86_64',
                'os': 'mac',
                'os_platform': 'osx-10-7',
                'vm': False}}),

 ('Rev4 MacOSX Lion 10.7 mozilla-inbound debug test reftest',
  {'build_type': 'debug',
   'job_type': 'unittest',
   'platform': {'arch': 'x86_64',
                'os': 'mac',
                'os_platform': 'osx-10-7',
                'vm': False}}),

 ('Rev4 MacOSX Lion 10.7 mozilla-inbound talos dromaeojs',
  {'build_type': 'opt',
   'job_type': 'talos',
   'platform': {'arch': 'x86_64',
                'os': 'mac',
                'os_platform': 'osx-10-7',
                'vm': False}}),

 ('Rev4 MacOSX Snow Leopard 10.6 mozilla-inbound debug test crashtest',
  {'build_type': 'debug',
   'job_type': 'unittest',
   'platform': {'arch': 'x86_64',
                'os': 'mac',
                'os_platform': 'osx-10-6',
                'vm': False}}),

 ('Rev5 MacOSX Mountain Lion 10.8 mozilla-inbound debug test crashtest',
  {'build_type': 'debug',
   'job_type': 'unittest',
   'platform': {'arch': 'x86_64',
                'os': 'mac',
                'os_platform': 'osx-10-8',
                'vm': False}}),

 ('Ubuntu ASAN VM 12.04 x64 mozilla-inbound opt test crashtest',
  {'build_type': 'opt',
   'job_type': 'unittest',
   'platform': {'arch': 'x86_64',
                'os': 'linux',
                'os_platform': 'linux64',
                'vm': True}}),

 ('Ubuntu VM 12.04 x64 mozilla-inbound debug test marionette',
  {'build_type': 'debug',
   'job_type': 'unittest',
   'platform': {'arch': 'x86_64',
                'os': 'linux',
                'os_platform': 'linux64',
                'vm': True}}),

 ('Ubuntu HW 12.04 mozilla-inbound pgo talos chromez',
  {'build_type': 'pgo',
   'job_type': 'talos',
   'platform': {'arch': 'x86',
                'os': 'linux',
                'os_platform': 'linux32',
                'vm': False}}),

 ('Ubuntu HW 12.04 x64 mozilla-inbound pgo talos chromez',
  {'build_type': 'pgo',
   'job_type': 'talos',
   'platform': {'arch': 'x86_64',
                'os': 'linux',
                'os_platform': 'linux64',
                'vm': False}}),

 ('Ubuntu VM 12.04 mozilla-inbound debug test crashtest',
  {'build_type': 'debug',
   'job_type': 'unittest',
   'platform': {'arch': 'x86',
                'os': 'linux',
                'os_platform': 'linux32',
                'vm': True}}),

 ('Ubuntu VM 12.04 x64 mozilla-inbound debug test crashtest',
  {'build_type': 'debug',
   'job_type': 'unittest',
   'platform': {'arch': 'x86_64',
                'os': 'linux',
                'os_platform': 'linux64',
                'vm': True}}),

 ('Windows 7 32-bit mozilla-inbound debug test crashtest',
  {'build_type': 'debug',
   'job_type': 'unittest',
   'platform': {'arch': 'x86',
                'os': 'win',
                'os_platform': 'windows7-32',
                'vm': False}}),

 ('Windows XP 32-bit mozilla-inbound debug test crashtest',
  {'build_type': 'debug',
   'job_type': 'unittest',
   'platform': {'arch': 'x86',
                'os': 'win',
                'os_platform': 'windowsxp',
                'vm': False}}),

 ('WINNT 5.2 mozilla-inbound build',
  {'build_type': 'opt',
   'job_type': 'build',
   'platform': {'arch': 'x86',
                'os': 'win',
                'os_platform': 'windowsxp',
                'vm': False}}),

 ('WINNT 6.2 mozilla-inbound debug test crashtest',
  {'build_type': 'debug',
   'job_type': 'unittest',
   'platform': {'arch': 'x86',
                'os': 'win',
                'os_platform': 'windows8-32',
                'vm': False}})
]


@slow
@pytest.mark.parametrize(('buildername', 'exp_result'), buildernames)
def test_extract_platform_info(buildername, exp_result):
    """
    test getting the right platform based on the buildername
    """

    result = buildbot.extract_platform_info(buildername)

    assert result == exp_result["platform"]


@slow
@pytest.mark.parametrize(('buildername', 'exp_result'), buildernames)
def test_extract_job_type_info(buildername, exp_result):
    """
    test getting the right job_type based on the buildername
    """

    result = buildbot.extract_job_type(buildername)

    assert result == exp_result["job_type"]


@slow
@pytest.mark.parametrize(('buildername', 'exp_result'), buildernames)
def test_extract_build_type(buildername, exp_result):
    """
    test getting the right platform based on the buildername
    """

    result = buildbot.extract_build_type(buildername)

    assert result == exp_result["build_type"]
