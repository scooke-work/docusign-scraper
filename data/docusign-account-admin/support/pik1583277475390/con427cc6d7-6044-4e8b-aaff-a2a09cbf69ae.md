---
title: ID Verification for NYCRR500 Compliance Configuration
source_url: https://support.docusign.com/s/document-item?language=en_US&bundleId=pik1583277475390&topicId=con427cc6d7-6044-4e8b-aaff-a2a09cbf69ae.html&_LANG=enus
site: support.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T23:38:35Z'
---

# ID Verification for NYCRR500 Compliance Configuration

Read about the ID Verification for NYCRR500 Compliance configuration. This ID Verification configuration helps organizations to comply with the 23 NYCRR Part 500 cybersecurity regulation for U.S.-based recipients.

ID Verification for NYCRR500 Compliance is an ID Verification configuration that helps organizations operating in New York, United States (U.S.), comply with the 23 NYCRR Part 500 cybersecurity regulation. The New York State Department of Financial Services (NYDFS) issued this regulation. It requires covered entities in the Financial Services sector to implement Multi-Factor Authentication (MFA) and conduct risk assessments to protect nonpublic information.

The ID Verification for NYCRR500 Compliance configuration combines a live risk assessment with a two-factor authentication sequence in a single recipient experience. Docusign works with a trusted partner (Socure) to perform recipients’ risk assessment.

If the assessment is successful, recipients must comply with Knowledge-Based Authentication to verify their identity. Eventually, if ID Verification confirms the recipients’ identity, they proceed to Phone Authentication and receive a one-time passcode (OTP) to access the envelope. This step sequence satisfies the MFA requirement of 23 NYCRR Part 500.

Note: Docusign recommends that organizations consult with their legal counsel to determine if ID Verification for NYCRR500 Compliance helps them meet their compliance requirements under 23 NYCRR Part 500.

## Use cases

ID Verification for NYCRR500 Compliance can help organizations ensure security and regulatory compliance in the following situations:

- Banking and lending: ID Verification checks borrower identities before signing high-value loan agreements or opening retail accounts.
- Insurance: ID Verification for NYCRR500 Compliance authenticates policyholders and claimants for sensitive digital transactions.
- Wealth management: ID Verification for NYCRR500 Compliance secures account transfers and high-risk investment authorizations with an audit-ready MFA trail.
- Fintech: ID Verification reduces fraud during digital onboarding while maintaining compliance with New York's cybersecurity framework.

## Availability and limitations

The ID Verification for NYCRR500 Compliance configuration is available only for account plans that include ID Verification, ID Verification Premier, or IAM for CX. It is only available to Docusign accounts hosted in the U.S.-based datacenters. Recipients applying for this ID Verification configuration must be U.S. residents or U.S. citizens with a valid SSN (Social Security number) and a U.S. address.

ID Verification for NYCRR500 Compliance is a read-only configuration. You cannot edit its parameters.

## ID Verification for NYCRR500 Compliance configuration

Identity Verification provides a read-only configuration for ID Verification for NYCRR500 Compliance. You cannot edit its parameters. This configuration includes the following parameters:

- Name and description: The name and description display to senders when they select an identity verification method for their envelope recipients.
- Maximum verification attempts: Recipients can attempt up to 4 unsuccessful verifications. Beyond this limit, the envelope locks automatically.
- Name Variation level: ID Verification accepts maximum variation for name matching, as explained in the [ID Name Matching](https://support.docusign.com/s/document-item?bundleId=ced1643229641057&topicId=rhb1657542911402.html&_LANG=enus) help page.
- Recipient must verify: ID Verification requires recipients to verify their identity every time they access the envelope.
- Workflow: Recipients must comply with strict ID Verification methods to satisfy the MFA requirement of 23 NYCRR Part 500. For more information, read the [ID Verification for NYCRR500 Compliance workflow](https://support.docusign.com/s/document-item?language=en_US&bundleId=pik1583277475390&topicId=con427cc6d7-6044-4e8b-aaff-a2a09cbf69ae.html&_LANG=enus&anchor=con427cc6d7-6044-4e8b-aaff-a2a09cbf69ae__id-verification-for-nycrr500-compliance-workflow) section.
- Data to store: ID Evidence stores all the authentication events and risk signals. This record helps organizations maintain the documentation they need for regulatory reporting and audit purposes under 23 NYCRR Part 500.

## ID Verification for NYCRR500 Compliance workflow

The workflow for verifying recipients' compliance with the 23 NYCRR Part 500 cybersecurity regulation includes the following steps:

1. Risk assessment: ID Verification asks recipients to submit a set of information that the trusted partner (Socure) analyzes to determine the appropriate risk level. For example, an email domain listed as high risk can increase the risk score. Docusign administrators cannot change the risk assessment parameters. If their risk score is satisfactory, recipients can proceed with Knowledge-Based Authentication. For more information about the reasons for risk assessment failure, read the [Rejection criteria](https://support.docusign.com/s/document-item?language=en_US&bundleId=pik1583277475390&topicId=con427cc6d7-6044-4e8b-aaff-a2a09cbf69ae.html&_LANG=enus&anchor=con427cc6d7-6044-4e8b-aaff-a2a09cbf69ae__rejection-criteria) section.
2. Knowledge-Based Authentication (KBA): ID Verification asks the recipients to answer a series of questions based on their public records, such as their current home address. If the recipients’ answers are correct, ID Verification approves their identity and allows access to the Phone Authentication step.
3. Phone Authentication: ID Verification sends a one-time passcode (OTP) through SMS or phone call to recipients. This step confirms that the recipient possesses a verified device. If the submitted code is correct, recipients can access the envelope.

This three-step sequence satisfies the MFA requirement of 23 NYCRR Part 500.

## Rejection criteria

The Reject Recipients section lists the triggers that automatically block recipients during the risk assessment process. Administrators cannot change those parameters.

- Almost certain probability of fraud: ID Verification blocks recipients when the trusted partner detects a high probability of fraud based on data analysis.
- Date of birth indicates COPPA review: ID Verification blocks recipients when the provided date of birth indicates they are under 13 years old. This trigger requires a review under the Children's Online Privacy Protection Act (COPPA).
- Email or IP address in a sanctioned country: ID Verification blocks recipients when their email or IP address originates from a country listed in the OFAC (Office of Foreign Assets Control) database.
- Social Security Number has been reported as deceased: ID Verification blocks recipients when the Social Security Administration reports the provided Social Security Number as deceased.
- Global Watchlist Screening: ID Verification blocks recipients when the trusted partner finds that recipients display on the AML (Anti-Money Laundering) or the OFAC list. However, recipients displaying on the PEP (Politically Exposed Persons) or Adverse Media lists can still complete the verification process.

## Data to store

ID Evidence captures all relevant information occurring during ID Verification for NYCRR500 Compliance. This data provides a unified, tamper-evident record of the verification process.

ID Evidence records the following risk assessment metadata:

- Risk level: ID Verification can assign recipients a Low, Medium, High, or Reject profile.
- Personal Information: ID Evidence captures recipients’ first and last names, date of birth, and gender.
- Risk-assessment details: ID Evidence shows the data that recipients submitted for risk assessment, and that the trusted partner flagged as High risk or Neutral. For example, if a recipient submits an invalid or nonexistent address, the trusted partner flags this information as high risk.

When recipients proceed with Knowledge-Based Authentication, ID Evidence captures the following information:

- Verification status and timestamps: ID Evidence indicates if the recipient passed the authentication and when the verification occurred.
- Type of ID: ID Evidence records the type of ID document that recipients submitted and the country or region they selected.
- Quiz results: ID Evidence stores the number of questions asked to recipients and the number of correct answers.
- Identity data: ID Evidence shows the date of birth and address that the recipient submitted.
- Envelope ID: ID Evidence returns the ID of the envelope that the recipient is trying to access.

ID Evidence also stores the verification status of the Phone Authentication process.
