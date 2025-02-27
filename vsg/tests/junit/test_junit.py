
import unittest
import platform

from vsg import junit

class testJunitClasses(unittest.TestCase):


    def test_failure_class_attributes(self):
        oFailure = junit.failure('Type1')
        self.assertTrue(oFailure)
        self.assertEqual(oFailure.type, 'Type1')
        self.assertEqual(oFailure.text, None)

    def test_failure_class_add_text(self):
        oFailure = junit.failure('type')
        oFailure.add_text('Text1')
        oFailure.add_text('Text2')
        oFailure.add_text('Text3')
        self.assertEqual(oFailure.type, 'type')
        self.assertEqual(oFailure.text[0], 'Text1')
        self.assertEqual(oFailure.text[1], 'Text2')
        self.assertEqual(oFailure.text[2], 'Text3')

    def test_failure_class_build_junit(self):
        oFailure = junit.failure('type')
        oFailure.add_text('Text1')
        oFailure.add_text('Text2')
        oFailure.add_text('Text3')
        dExpected = []
        dExpected.append('    <failure type="type">')
        dExpected.append('      Text1')
        dExpected.append('      Text2')
        dExpected.append('      Text3')
        dExpected.append('    </failure>')
        self.assertEqual(dExpected, oFailure.build_junit())

    def test_testcase_class_attributes(self):
        oTestcase = junit.testcase()
        self.assertTrue(oTestcase)
        self.assertEqual(oTestcase.name, None)
        self.assertEqual(oTestcase.time, None)
        self.assertEqual(oTestcase.failures, None)

    def test_testcase_class_attribute_setting(self):
        oTestcase = junit.testcase('Name', 'Time')
        self.assertEqual(oTestcase.name, 'Name')
        self.assertEqual(oTestcase.time, 'Time')
        self.assertEqual(oTestcase.failures, None)

    def test_testcase_class_add_failure(self):
        oTestcase = junit.testcase('Name', 'Time')
        oTestcase.add_failure(junit.failure('Type1'))
        oTestcase.add_failure(junit.failure('Type2'))
        oTestcase.add_failure(junit.failure('Type3'))
        self.assertEqual(oTestcase.failures[0].type, 'Type1')
        self.assertEqual(oTestcase.failures[1].type, 'Type2')
        self.assertEqual(oTestcase.failures[2].type, 'Type3')

    def test_testcase_class_build_junit(self):
        oTestcase = junit.testcase('Name', 'Time')
        for i in range(0, 3):
            oFailure = junit.failure('Type' + str(i))
            for j in range(0, 3):
                oFailure.add_text('Text_' + str(i) + '_' + str(j))
            oTestcase.add_failure(oFailure)
        dExpected = []
        dExpected.append('  <testcase name="Name" time="Time">')
        dExpected.append('    <failure type="Type0">')
        dExpected.append('      Text_0_0')
        dExpected.append('      Text_0_1')
        dExpected.append('      Text_0_2')
        dExpected.append('    </failure>')
        dExpected.append('    <failure type="Type1">')
        dExpected.append('      Text_1_0')
        dExpected.append('      Text_1_1')
        dExpected.append('      Text_1_2')
        dExpected.append('    </failure>')
        dExpected.append('    <failure type="Type2">')
        dExpected.append('      Text_2_0')
        dExpected.append('      Text_2_1')
        dExpected.append('      Text_2_2')
        dExpected.append('    </failure>')
        dExpected.append('  </testcase>')
        self.assertEqual(dExpected, oTestcase.build_junit())

    def test_testsuite_class_attributes(self):
        oTestsuite = junit.testsuite('Name', 'Time')
        self.assertTrue(oTestsuite)
        self.assertEqual(oTestsuite.name, 'Name')
        self.assertEqual(oTestsuite.time, 'Time')
        self.assertEqual(oTestsuite.testcases, None)
        self.assertEqual(oTestsuite.timestamp, oTestsuite.timestamp)

    def test_testsuite_class_add_testcase(self):
        oTestsuite = junit.testsuite('Name', 'Time')
        oTestsuite.add_testcase(junit.testcase('TC_Name0', 'TC_Time0'))
        oTestsuite.add_testcase(junit.testcase('TC_Name1', 'TC_Time1'))
        oTestsuite.add_testcase(junit.testcase('TC_Name2', 'TC_Time2'))
        self.assertEqual(oTestsuite.testcases[0].name, 'TC_Name0')
        self.assertEqual(oTestsuite.testcases[1].name, 'TC_Name1')
        self.assertEqual(oTestsuite.testcases[2].name, 'TC_Name2')

    def test_testsuite_class_build_junit(self):
        oTestsuite = junit.testsuite('TS_Name', 'TS_Time')
        for k in range(0, 3):
            oTestcase = junit.testcase('Name' + str(k), 'Time' + str(k))
            for i in range(0, 3):
                oFailure = junit.failure('Type' + str(i))
                for j in range(0, 3):
                    oFailure.add_text('Text_' + str(i) + '_' + str(j))
                oTestcase.add_failure(oFailure)
            oTestsuite.add_testcase(oTestcase)

        sHostname = platform.uname()[1]

        dExpected = []
        dExpected.append('<testsuite errors="0" hostname="' + sHostname + '" failures="9" timestamp="' + oTestsuite.timestamp + '" tests="3" time="TS_Time" name="TS_Name">')
        dExpected.append('  <properties>')
        dExpected.append('  </properties>')
        dExpected.append('  <testcase name="Name0" time="Time0">')
        dExpected.append('    <failure type="Type0">')
        dExpected.append('      Text_0_0')
        dExpected.append('      Text_0_1')
        dExpected.append('      Text_0_2')
        dExpected.append('    </failure>')
        dExpected.append('    <failure type="Type1">')
        dExpected.append('      Text_1_0')
        dExpected.append('      Text_1_1')
        dExpected.append('      Text_1_2')
        dExpected.append('    </failure>')
        dExpected.append('    <failure type="Type2">')
        dExpected.append('      Text_2_0')
        dExpected.append('      Text_2_1')
        dExpected.append('      Text_2_2')
        dExpected.append('    </failure>')
        dExpected.append('  </testcase>')
        dExpected.append('  <testcase name="Name1" time="Time1">')
        dExpected.append('    <failure type="Type0">')
        dExpected.append('      Text_0_0')
        dExpected.append('      Text_0_1')
        dExpected.append('      Text_0_2')
        dExpected.append('    </failure>')
        dExpected.append('    <failure type="Type1">')
        dExpected.append('      Text_1_0')
        dExpected.append('      Text_1_1')
        dExpected.append('      Text_1_2')
        dExpected.append('    </failure>')
        dExpected.append('    <failure type="Type2">')
        dExpected.append('      Text_2_0')
        dExpected.append('      Text_2_1')
        dExpected.append('      Text_2_2')
        dExpected.append('    </failure>')
        dExpected.append('  </testcase>')
        dExpected.append('  <testcase name="Name2" time="Time2">')
        dExpected.append('    <failure type="Type0">')
        dExpected.append('      Text_0_0')
        dExpected.append('      Text_0_1')
        dExpected.append('      Text_0_2')
        dExpected.append('    </failure>')
        dExpected.append('    <failure type="Type1">')
        dExpected.append('      Text_1_0')
        dExpected.append('      Text_1_1')
        dExpected.append('      Text_1_2')
        dExpected.append('    </failure>')
        dExpected.append('    <failure type="Type2">')
        dExpected.append('      Text_2_0')
        dExpected.append('      Text_2_1')
        dExpected.append('      Text_2_2')
        dExpected.append('    </failure>')
        dExpected.append('  </testcase>')
        dExpected.append('  <system-out>')
        dExpected.append('  </system-out>')
        dExpected.append('  <system-err>')
        dExpected.append('  </system-err>')
        dExpected.append('</testsuite>')
        self.assertEqual(dExpected, oTestsuite.build_junit())

    def test_xmlfile_class_attributes(self):
        oXmlfile = junit.xmlfile('FileName')
        self.assertTrue(oXmlfile)
        self.assertEqual(oXmlfile.filename, 'FileName')
        self.assertEqual(oXmlfile.testsuites, None)

    def test_xmlfile_class_add_testsuite(self):
        oXmlfile = junit.xmlfile('FileName')
        oXmlfile.add_testsuite(junit.testsuite('TS_NAME0', 'TS_TIME0'))
        oXmlfile.add_testsuite(junit.testsuite('TS_NAME1', 'TS_TIME1'))
        oXmlfile.add_testsuite(junit.testsuite('TS_NAME2', 'TS_TIME2'))
        self.assertEqual(oXmlfile.testsuites[0].name, 'TS_NAME0')
        self.assertEqual(oXmlfile.testsuites[1].name, 'TS_NAME1')
        self.assertEqual(oXmlfile.testsuites[2].name, 'TS_NAME2')

    def test_xmlfile_class_build_junit(self):
        oXmlfile = junit.xmlfile('FileName')
        for x in range(0,2):
            oTestsuite = junit.testsuite('TS_Name' + str(x), 'TS_Time' + str(x))
            for k in range(0, 3):
                oTestcase = junit.testcase('Name' + str(k), 'Time' + str(k))
                for i in range(0, 3):
                    oFailure = junit.failure('Type' + str(i))
                    for j in range(0, 3):
                        oFailure.add_text('Text_' + str(i) + '_' + str(j))
                    oTestcase.add_failure(oFailure)
                oTestsuite.add_testcase(oTestcase)
            oXmlfile.add_testsuite(oTestsuite)

        sHostname = platform.uname()[1]

        dExpected = []
        dExpected.append('<?xml version="1.0" ?>')
        dExpected.append('<testsuite errors="0" hostname="' + sHostname + '" failures="9" timestamp="' + oTestsuite.timestamp + '" tests="3" time="TS_Time0" name="TS_Name0">')
        dExpected.append('  <properties>')
        dExpected.append('  </properties>')
        dExpected.append('  <testcase name="Name0" time="Time0">')
        dExpected.append('    <failure type="Type0">')
        dExpected.append('      Text_0_0')
        dExpected.append('      Text_0_1')
        dExpected.append('      Text_0_2')
        dExpected.append('    </failure>')
        dExpected.append('    <failure type="Type1">')
        dExpected.append('      Text_1_0')
        dExpected.append('      Text_1_1')
        dExpected.append('      Text_1_2')
        dExpected.append('    </failure>')
        dExpected.append('    <failure type="Type2">')
        dExpected.append('      Text_2_0')
        dExpected.append('      Text_2_1')
        dExpected.append('      Text_2_2')
        dExpected.append('    </failure>')
        dExpected.append('  </testcase>')
        dExpected.append('  <testcase name="Name1" time="Time1">')
        dExpected.append('    <failure type="Type0">')
        dExpected.append('      Text_0_0')
        dExpected.append('      Text_0_1')
        dExpected.append('      Text_0_2')
        dExpected.append('    </failure>')
        dExpected.append('    <failure type="Type1">')
        dExpected.append('      Text_1_0')
        dExpected.append('      Text_1_1')
        dExpected.append('      Text_1_2')
        dExpected.append('    </failure>')
        dExpected.append('    <failure type="Type2">')
        dExpected.append('      Text_2_0')
        dExpected.append('      Text_2_1')
        dExpected.append('      Text_2_2')
        dExpected.append('    </failure>')
        dExpected.append('  </testcase>')
        dExpected.append('  <testcase name="Name2" time="Time2">')
        dExpected.append('    <failure type="Type0">')
        dExpected.append('      Text_0_0')
        dExpected.append('      Text_0_1')
        dExpected.append('      Text_0_2')
        dExpected.append('    </failure>')
        dExpected.append('    <failure type="Type1">')
        dExpected.append('      Text_1_0')
        dExpected.append('      Text_1_1')
        dExpected.append('      Text_1_2')
        dExpected.append('    </failure>')
        dExpected.append('    <failure type="Type2">')
        dExpected.append('      Text_2_0')
        dExpected.append('      Text_2_1')
        dExpected.append('      Text_2_2')
        dExpected.append('    </failure>')
        dExpected.append('  </testcase>')
        dExpected.append('  <system-out>')
        dExpected.append('  </system-out>')
        dExpected.append('  <system-err>')
        dExpected.append('  </system-err>')
        dExpected.append('</testsuite>')
        dExpected.append('<testsuite errors="0" hostname="' + sHostname + '" failures="9" timestamp="' + oTestsuite.timestamp + '" tests="3" time="TS_Time1" name="TS_Name1">')
        dExpected.append('  <properties>')
        dExpected.append('  </properties>')
        dExpected.append('  <testcase name="Name0" time="Time0">')
        dExpected.append('    <failure type="Type0">')
        dExpected.append('      Text_0_0')
        dExpected.append('      Text_0_1')
        dExpected.append('      Text_0_2')
        dExpected.append('    </failure>')
        dExpected.append('    <failure type="Type1">')
        dExpected.append('      Text_1_0')
        dExpected.append('      Text_1_1')
        dExpected.append('      Text_1_2')
        dExpected.append('    </failure>')
        dExpected.append('    <failure type="Type2">')
        dExpected.append('      Text_2_0')
        dExpected.append('      Text_2_1')
        dExpected.append('      Text_2_2')
        dExpected.append('    </failure>')
        dExpected.append('  </testcase>')
        dExpected.append('  <testcase name="Name1" time="Time1">')
        dExpected.append('    <failure type="Type0">')
        dExpected.append('      Text_0_0')
        dExpected.append('      Text_0_1')
        dExpected.append('      Text_0_2')
        dExpected.append('    </failure>')
        dExpected.append('    <failure type="Type1">')
        dExpected.append('      Text_1_0')
        dExpected.append('      Text_1_1')
        dExpected.append('      Text_1_2')
        dExpected.append('    </failure>')
        dExpected.append('    <failure type="Type2">')
        dExpected.append('      Text_2_0')
        dExpected.append('      Text_2_1')
        dExpected.append('      Text_2_2')
        dExpected.append('    </failure>')
        dExpected.append('  </testcase>')
        dExpected.append('  <testcase name="Name2" time="Time2">')
        dExpected.append('    <failure type="Type0">')
        dExpected.append('      Text_0_0')
        dExpected.append('      Text_0_1')
        dExpected.append('      Text_0_2')
        dExpected.append('    </failure>')
        dExpected.append('    <failure type="Type1">')
        dExpected.append('      Text_1_0')
        dExpected.append('      Text_1_1')
        dExpected.append('      Text_1_2')
        dExpected.append('    </failure>')
        dExpected.append('    <failure type="Type2">')
        dExpected.append('      Text_2_0')
        dExpected.append('      Text_2_1')
        dExpected.append('      Text_2_2')
        dExpected.append('    </failure>')
        dExpected.append('  </testcase>')
        dExpected.append('  <system-out>')
        dExpected.append('  </system-out>')
        dExpected.append('  <system-err>')
        dExpected.append('  </system-err>')
        dExpected.append('</testsuite>')
        self.assertEqual(dExpected, oXmlfile.build_junit())

    def test_xmlfile_class_no_failures_build_junit(self):
        self.maxDiff = None
        oXmlfile = junit.xmlfile('FileName')
        for x in range(0,2):
            oTestsuite = junit.testsuite('TS_Name' + str(x), 'TS_Time' + str(x))
            for k in range(0, 3):
                oTestcase = junit.testcase('Name' + str(k), 'Time' + str(k))
                oTestsuite.add_testcase(oTestcase)
            oXmlfile.add_testsuite(oTestsuite)

        sHostname = platform.uname()[1]

        dExpected = []
        dExpected.append('<?xml version="1.0" ?>')
        dExpected.append('<testsuite errors="0" hostname="' + sHostname + '" failures="0" timestamp="' + oTestsuite.timestamp + '" tests="3" time="TS_Time0" name="TS_Name0">')
        dExpected.append('  <properties>')
        dExpected.append('  </properties>')
        dExpected.append('  <testcase name="Name0" time="Time0">')
        dExpected.append('  </testcase>')
        dExpected.append('  <testcase name="Name1" time="Time1">')
        dExpected.append('  </testcase>')
        dExpected.append('  <testcase name="Name2" time="Time2">')
        dExpected.append('  </testcase>')
        dExpected.append('  <system-out>')
        dExpected.append('  </system-out>')
        dExpected.append('  <system-err>')
        dExpected.append('  </system-err>')
        dExpected.append('</testsuite>')
        dExpected.append('<testsuite errors="0" hostname="' + sHostname + '" failures="0" timestamp="' + oTestsuite.timestamp + '" tests="3" time="TS_Time1" name="TS_Name1">')
        dExpected.append('  <properties>')
        dExpected.append('  </properties>')
        dExpected.append('  <testcase name="Name0" time="Time0">')
        dExpected.append('  </testcase>')
        dExpected.append('  <testcase name="Name1" time="Time1">')
        dExpected.append('  </testcase>')
        dExpected.append('  <testcase name="Name2" time="Time2">')
        dExpected.append('  </testcase>')
        dExpected.append('  <system-out>')
        dExpected.append('  </system-out>')
        dExpected.append('  <system-err>')
        dExpected.append('  </system-err>')
        dExpected.append('</testsuite>')
        self.assertEqual(dExpected, oXmlfile.build_junit())

    def test_escape_xml_characters(self):
        self.assertEqual('&lt;', junit.escape_xml_characters('<'))
        self.assertEqual('&gt;', junit.escape_xml_characters('>'))
        self.assertEqual('&quot;', junit.escape_xml_characters('"'))
        self.assertEqual('&apos;', junit.escape_xml_characters('\''))
        self.assertEqual('&amp;', junit.escape_xml_characters('&'))
        self.assertEqual('&amp;&lt;&gt;&amp;&gt;&lt;&apos;&quot;&amp;&quot;&apos;&gt;&quot;&gt;&lt;&amp;&apos;&quot;', junit.escape_xml_characters('&<>&><\'"&"\'>"><&\'"'))
