Amazon AppFlow is a fully managed integration service that enables you to securely transfer data between Software-as-a-Service (SaaS) applications like Salesforce, Marketo, Slack, and ServiceNow, and AWS services like Amazon S3 and Amazon Redshift, in just a few clicks.


https://catalog.us-east-1.prod.workshops.aws/workshops/9787ec94-1ace-44cc-91e5-976ad7ddc0b1/en-US/salesforce/salesforce2redshift/redshiftsetup # redshift setup 

Creating an Amazon Redshift cluster using an AWS Cloudformation 
This template allows you to standardize the Amazon Redshift Cluster's creation to meet your organizational infrastructure and security standards. 

Getting ready: 

- Set Up the Salesforce AWS Integration: https://hevodata.com/lea rn/salesforce-aws-integration/#Steps
https://docs.aws.amazon.com/connect/latest/adminguide/integrate-salesforce-tasks.html

        ---  1: Set Up an Amazon Create Instance
The Salesforce AWS Integration process starts from your AWS account. Enter “amazon connect” in the search bar and select the Amazon Connect option. Another way to find it is by expanding the All Services section and scrolling down to the Customer Experience category. 
        --- 
        ---

- Cloudformation 6 templates:
            1.Salesforce_CustomCase
            2.Salesforce_Account
            3.Salesforce_Opportunity
            4.Salesforce_Contact
            5.Salesforce_Case
            6.AWSPOC_Account 

- Create an IAM user with access to AWS CloudFormation
- Amazon Redshift cluster 
- create Lambda function 
- create role 
- Create S3 bucket   - optional 
                Choose an S3 bucket to write any records that couldn't be written to the destination. Write data that couldn't be transfered
- Create KMS 





Salesforce Signup
Salesforce is a leading Cloud based CRM solution provider. Salesforce can be used as a source or destination of a flow built with AppFlow.

Use the following steps to register a trial Salesforce account. Note: The Salesforce lab in this workshop requires that you have a developer edition trial account created in Salesforce. If you already have one available you can skip the "Sign Up Section" and proceed to enabling change data capture section.


Sign Up for Salesforce Developer Edition trial
Go to https://developer.Salesforce.com/signup  and register for a trial of the Developer Edition account in Salesforce. Make sure you provide a valid and an accessible email address since you will receive a verification email from Salesforce.




