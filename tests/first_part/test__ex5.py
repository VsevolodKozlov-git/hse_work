import unittest
import re

from exercises.first_part import ex5


class RegexTests(unittest.TestCase):
    t1 = "In an upcoming survey, we are gearing up to engage with a diverse set of individuals, each bringing their unique perspectives to the table. Although the survey has yet to be conducted, we have gathered initial information on some potential respondents. Firstly, we have Sarah Johnson, a 28-year-old female, who has shown keen interest in participating. You can reach her at (999) 123-4567. John Smith, a 42-year-old male, has also expressed interest in taking part, and you can contact him at (912) 987-6543. Additionally, we've received an expression of interest from Maria Rodriguez, a 35-year-old female, with a contact number of (908) 789-0123. James Anderson, a 50-year-old male, is considering participation and can be reached at (911) 234-5678. Sophia Lee, a 23-year-old female, has shown interest in contributing to the survey, and you can reach her at (909) 456-7890. Lastly, Robert Davis, a 60-year-old male, with a contact number of (977) 345-6789, is another prospective respondent eager to provide insights."

    def test1(self):
        print(re.findall(r'\b(\d+)-year-old', self.t1))



class Tests(unittest.TestCase):

    def test_interview(self):
        report = "In an upcoming survey, we're preparing to engage with a diverse group of individuals. While the survey has not yet taken place, we have preliminary information about potential respondents. Sarah Johnson, a 32-year-old female, has expressed interest in participating and provided her contact number as (914) 123-4567. John Smith, a 45-year-old male, is another prospective respondent with a contact number of (961) 987-6543. Emily Davis, a 28-year-old female, may contribute to the survey and can be reached at (911) 456-7890. Michael Brown, a 38-year-old male, is also considering participation with a contact number of (986) 234-5678. We've received interest from Olivia Wilson, a 27-year-old female, who may join the survey, and her contact number is (945) 789-0123. David Lee, a 52-year-old male, has shown interest with a contact number of (977) 345-6789."
        actual_result = ex5.refine_interview(report, 'female')
        expected_result = [{'name': 'Sarah Johnson', 'age': 32, 'gender': 'female', 'phone number': '+7-914-123-45-67'},
{'name': 'Emily Davis', 'age': 28, 'gender': 'female', 'phone number': '+7-911-456-78-90'},
{'name': 'Olivia Wilson', 'age': 27, 'gender': 'female', 'phone number': '+7-945-789-01-23'}]
        self.assertEqual(actual_result, expected_result)

        report ="In an upcoming survey, we are gearing up to engage with a diverse set of individuals, each bringing their unique perspectives to the table. Although the survey has yet to be conducted, we have gathered initial information on some potential respondents. Firstly, we have Sarah Johnson, a 28-year-old female, who has shown keen interest in participating. You can reach her at (999) 123-4567. John Smith, a 42-year-old male, has also expressed interest in taking part, and you can contact him at (912) 987-6543. Additionally, we've received an expression of interest from Maria Rodriguez, a 35-year-old female, with a contact number of (908) 789-0123. James Anderson, a 50-year-old male, is considering participation and can be reached at (911) 234-5678. Sophia Lee, a 23-year-old female, has shown interest in contributing to the survey, and you can reach her at (909) 456-7890. Lastly, Robert Davis, a 60-year-old male, with a contact number of (977) 345-6789, is another prospective respondent eager to provide insights."
        ex5.refine_interview(report, 'male', 45)
        expected_result =[{'name': 'Sarah Johnson', 'age': 32, 'gender': 'female', 'phone number': '+7-914-123-45-67'},
{'name': 'Emily Davis', 'age': 28, 'gender': 'female', 'phone number': '+7-911-456-78-90'},
{'name': 'Olivia Wilson', 'age': 27, 'gender': 'female', 'phone number': '+7-945-789-01-23'}]
        self.assertEqual(actual_result, expected_result)

        # report =
        # ex5.refine_interview(report, 'female')
        # expected_result =
        # self.assertEqual(actual_result, expected_result)

    def test_marketing(self):
        report = "In our assessment of various Russian companies, we have identified several that stand out in terms of their financial performance and adherence to government standards. One such impressive company is Petrovich Electronics Ltd., with a website URL at www.petrovichelectronics.ru. It reported a last year income of $25,000,000 and a profit of $5,000,000. Petrovich Electronics Ltd. has a TIN number of 7701234567. Siberian Steelworks Inc., accessible at www.siberiansteelworks.ru, generated a last year income of $60,000,000 and a profit of $10,000,000. The TIN number for Siberian Steelworks Inc. is 7709876543. MosTech Solutions LLC, whose website URL is www.mostechsolutions.ru, is another notable company. With a last year income of $40,000,000 and a profit of $8,000,000, MosTech Solutions LLC demonstrates strong financial performance. It has a TIN number of 3306543210. Volga Pharmaceuticals Ltd., found at www.volga-pharma.ru, recorded a last year income of $35,000,000 and a profit of $7,000,000. Volga Pharmaceuticals Ltd. also has a TIN number of 3404567890. Arctic Renewable Energy Corp., accessible via www.arcticrenewable.ru, is another standout company. It reported a last year income of $75,000,000 and a profit of $12,000,000. Arctic Renewable Energy Corp. has a TIN number of 8907890123."
        actual_result = ex5.refine_market(report, 0.2, 'Moscow')
        expected_result = [{'company name': 'Petrovich Electronics Ltd.', 'url': 'www.petrovichelectronics.ru.', 'TIN': 7701234567, 'income': 25000000, 'profit': 5000000}]
        self.assertEqual(actual_result, expected_result)

        report = "In our assessment of various Russian companies, we have identified several that stand out in terms of their financial performance and adherence to government standards. AeroTech Innovations Inc., with a website URL at www.aerotechinnovations.ru, reported a last year income of $45,000,000 and a profit of $9,000,000. AeroTech Innovations Inc. has a TIN number of 5501234567. TechSolutions Group LLC, whose website URL is www.techsolutionsgroup.ru, is another notable company. With a last year income of $65,000,000 and a profit of $11,000,000, TechSolutions Group LLC demonstrates strong financial performance. It has a TIN number of 3306543210. MediCare Pharmaceuticals Ltd., found at www.medicare-pharma.ru, recorded a last year income of $75,000,000 and a profit of $13,000,000. MediCare Pharmaceuticals Ltd. also has a TIN number of 6404567890. Northern Energy Solutions Corp., accessible via www.northernenergysolutions.ru, is another standout company. It reported a last year income of $95,000,000 and a profit of $18,000,000. Northern Energy Solutions Corp. has a TIN number of 7707890123."
        actual_result = ex5.refine_market(report)
        expected_result =   [{'company name': 'AeroTech Innovations Inc.', 'url': 'www.aerotechinnovations.ru', 'TIN': 5501234567, 'income': 45000000, 'profit': 9000000},
{'company name': 'TechSolutions Group LLC', 'url': 'www.techsolutionsgroup.ru', 'TIN': 3306543210, 'income': 65000000, 'profit': 11000000},
{'company name': 'MediCare Pharmaceuticals Ltd.', 'url': 'www.medicare-pharma.ru', 'TIN': 6404567890, 'income': 75000000, 'profit': 13000000},
{'company name': 'Northern Energy Solutions Corp.', 'url': 'www.northernenergysolutions.ru', 'TIN': 7707890123, 'income': 95000000, 'profit': 18000000}]

        self.assertEqual(actual_result, expected_result)

    def test_main(self):

        # different kwargs test interview
        report = "In an upcoming survey, we're preparing to engage with a diverse group of individuals. While the survey has not yet taken place, we have preliminary information about potential respondents. Sarah Johnson, a 32-year-old female, has expressed interest in participating and provided her contact number as (914) 123-4567. John Smith, a 45-year-old male, is another prospective respondent with a contact number of (961) 987-6543. Emily Davis, a 28-year-old female, may contribute to the survey and can be reached at (911) 456-7890. Michael Brown, a 38-year-old male, is also considering participation with a contact number of (986) 234-5678. We've received interest from Olivia Wilson, a 27-year-old female, who may join the survey, and her contact number is (945) 789-0123. David Lee, a 52-year-old male, has shown interest with a contact number of (977) 345-6789."
        actual_result = ex5.report_refiner(report, 'female', interview=True)
        expected_result = [{'name': 'Sarah Johnson', 'age': 32, 'gender': 'female', 'phone number': '+7-914-123-45-67'},
                           {'name': 'Emily Davis', 'age': 28, 'gender': 'female', 'phone number': '+7-911-456-78-90'},
                           {'name': 'Olivia Wilson', 'age': 27, 'gender': 'female', 'phone number': '+7-945-789-01-23'}]
        self.assertEqual(actual_result, expected_result)

        report = "In an upcoming survey, we're preparing to engage with a diverse group of individuals. While the survey has not yet taken place, we have preliminary information about potential respondents. Sarah Johnson, a 32-year-old female, has expressed interest in participating and provided her contact number as (914) 123-4567. John Smith, a 45-year-old male, is another prospective respondent with a contact number of (961) 987-6543. Emily Davis, a 28-year-old female, may contribute to the survey and can be reached at (911) 456-7890. Michael Brown, a 38-year-old male, is also considering participation with a contact number of (986) 234-5678. We've received interest from Olivia Wilson, a 27-year-old female, who may join the survey, and her contact number is (945) 789-0123. David Lee, a 52-year-old male, has shown interest with a contact number of (977) 345-6789."
        actual_result = ex5.report_refiner(report, 'female', market=False)
        expected_result = [{'name': 'Sarah Johnson', 'age': 32, 'gender': 'female', 'phone number': '+7-914-123-45-67'},
                           {'name': 'Emily Davis', 'age': 28, 'gender': 'female', 'phone number': '+7-911-456-78-90'},
                           {'name': 'Olivia Wilson', 'age': 27, 'gender': 'female', 'phone number': '+7-945-789-01-23'}]
        self.assertEqual(actual_result, expected_result)

        report = "In an upcoming survey, we're preparing to engage with a diverse group of individuals. While the survey has not yet taken place, we have preliminary information about potential respondents. Sarah Johnson, a 32-year-old female, has expressed interest in participating and provided her contact number as (914) 123-4567. John Smith, a 45-year-old male, is another prospective respondent with a contact number of (961) 987-6543. Emily Davis, a 28-year-old female, may contribute to the survey and can be reached at (911) 456-7890. Michael Brown, a 38-year-old male, is also considering participation with a contact number of (986) 234-5678. We've received interest from Olivia Wilson, a 27-year-old female, who may join the survey, and her contact number is (945) 789-0123. David Lee, a 52-year-old male, has shown interest with a contact number of (977) 345-6789."
        actual_result = ex5.report_refiner(report, 'female', interview=True, market=False)
        expected_result = [{'name': 'Sarah Johnson', 'age': 32, 'gender': 'female', 'phone number': '+7-914-123-45-67'},
                           {'name': 'Emily Davis', 'age': 28, 'gender': 'female', 'phone number': '+7-911-456-78-90'},
                           {'name': 'Olivia Wilson', 'age': 27, 'gender': 'female', 'phone number': '+7-945-789-01-23'}]
        self.assertEqual(actual_result, expected_result)

        #different kwargs test marketing

        report = "In our assessment of various Russian companies, we have identified several that stand out in terms of their financial performance and adherence to government standards. One such impressive company is Petrovich Electronics Ltd., with a website URL at www.petrovichelectronics.ru. It reported a last year income of $25,000,000 and a profit of $5,000,000. Petrovich Electronics Ltd. has a TIN number of 7701234567. Siberian Steelworks Inc., accessible at www.siberiansteelworks.ru, generated a last year income of $60,000,000 and a profit of $10,000,000. The TIN number for Siberian Steelworks Inc. is 7709876543. MosTech Solutions LLC, whose website URL is www.mostechsolutions.ru, is another notable company. With a last year income of $40,000,000 and a profit of $8,000,000, MosTech Solutions LLC demonstrates strong financial performance. It has a TIN number of 3306543210. Volga Pharmaceuticals Ltd., found at www.volga-pharma.ru, recorded a last year income of $35,000,000 and a profit of $7,000,000. Volga Pharmaceuticals Ltd. also has a TIN number of 3404567890. Arctic Renewable Energy Corp., accessible via www.arcticrenewable.ru, is another standout company. It reported a last year income of $75,000,000 and a profit of $12,000,000. Arctic Renewable Energy Corp. has a TIN number of 8907890123."
        expected_result = [
            {'company name': 'Petrovich Electronics Ltd.', 'url': 'www.petrovichelectronics.ru.', 'TIN': 7701234567,
             'income': 25000000, 'profit': 5000000}]

        actual_result = ex5.report_refiner(report, 0.2, 'Moscow', market=True)
        self.assertEqual(actual_result, expected_result)
        actual_result = ex5.report_refiner(report, 0.2, 'Moscow', interview=False)
        self.assertEqual(actual_result, expected_result)

        report = "In our assessment of various Russian companies, we have identified several that stand out in terms of their financial performance and adherence to government standards. AeroTech Innovations Inc., with a website URL at www.aerotechinnovations.ru, reported a last year income of $45,000,000 and a profit of $9,000,000. AeroTech Innovations Inc. has a TIN number of 5501234567. TechSolutions Group LLC, whose website URL is www.techsolutionsgroup.ru, is another notable company. With a last year income of $65,000,000 and a profit of $11,000,000, TechSolutions Group LLC demonstrates strong financial performance. It has a TIN number of 3306543210. MediCare Pharmaceuticals Ltd., found at www.medicare-pharma.ru, recorded a last year income of $75,000,000 and a profit of $13,000,000. MediCare Pharmaceuticals Ltd. also has a TIN number of 6404567890. Northern Energy Solutions Corp., accessible via www.northernenergysolutions.ru, is another standout company. It reported a last year income of $95,000,000 and a profit of $18,000,000. Northern Energy Solutions Corp. has a TIN number of 7707890123."
        expected_result = [
            {'company name': 'AeroTech Innovations Inc.', 'url': 'www.aerotechinnovations.ru', 'TIN': 5501234567,
             'income': 45000000, 'profit': 9000000},
            {'company name': 'TechSolutions Group LLC', 'url': 'www.techsolutionsgroup.ru', 'TIN': 3306543210,
             'income': 65000000, 'profit': 11000000},
            {'company name': 'MediCare Pharmaceuticals Ltd.', 'url': 'www.medicare-pharma.ru', 'TIN': 6404567890,
             'income': 75000000, 'profit': 13000000},
            {'company name': 'Northern Energy Solutions Corp.', 'url': 'www.northernenergysolutions.ru',
             'TIN': 7707890123, 'income': 95000000, 'profit': 18000000}]
        actual_result = ex5.report_refiner(report, market=True)
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
