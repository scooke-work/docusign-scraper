---
title: Risk Assessment Step
source_url: https://support.docusign.com/s/document-item?language=en_US&bundleId=yff1696971835267&topicId=con4af9cd30-8bb6-4ea9-a995-bb969aa1a7d2.html&_LANG=enus
site: support.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T18:04:36Z'
---

# Risk Assessment Step

Read about the Risk Assessment step, a Workflow Builder workflow
component that integrates dynamic participant risk signals to enable dynamic, data-driven
workflow orchestration and simplified compliance.

Risk Assessment is a step within a workflow that allows
process builders to integrate dynamic participant risk signals into their processes.
This step orchestrates intelligent workflows based on risk signals instead of static
assumptions. Participants submit personal information, such as their email address or
the last 4 digits of their Social Security number (SSN). The Docusign
trusted partner (Socure) then performs risk assessments and assigns participants a risk
score.

Process builders can retrieve Risk Assessment data from ID Evidence. They can also define subsequent steps for participants, based on their risk score.

## Risk Assessment use cases

Process builders can use Risk Assessment steps across the
following business scenarios:

- Financial account opening: Financial services use the Risk
  Assessment step to conduct compliance-driven identity
  verification during account creation processes.
- Loan and Credit Approval Workflows: The Risk Assessment
  process dynamically verifies borrowers' identity based on risk profiles.
- Insurance Claims Processing: Claimants proceed with the Risk
  Assessment step that streamlines or intensifies verification
  based on user risk.
- High-value Transactions: Risk Assessment dynamically
  tailors verification intensity based on transactional risk. Low-risk
  participants benefit from low-friction verification processes, while high-risk
  participants require more thorough checks.

## Risk Assessment step process

When process builders add a Risk Assessment step to their
workflow, they must select the participant data to request to determine the risk
profile. For example, they can decide that each selected participant must submit
their phone number. Next, process builders select the data they want to store in ID
Evidence and the participants whose data they want to assess.

When participants enter the Risk Assessment step, they submit
the requested data, such as their phone number or address. The trusted partner
analyzes the submitted data to determine the appropriate risk level. For example, if
participants provide their phone number, the trusted partner returns a "Phone number
risk" variable. The score of this variable determines the risk level based on the
number.

Based on all the participants' data, the Risk Assessment step
returns a risk category (high, medium, low), a numerical score, and detailed
explanations.

When participants complete the Risk Assessment step, they
proceed to the subsequent steps based on their risk score. For example, process
builders can decide that participants with a high-risk profile must submit their ID
with liveness verification to verify their identity. They can also redirect
participants with a medium-risk profile to Knowledge-based authentication and let
participants with a low-risk profile proceed in the workflow.

Note: For more information about adding ID Verification and Knowledge-based authentication to a workflow, read the [Verify Someone's Identity Step](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=uak1735246809132.html&_LANG=enus "Learn about Verify Someone's Identity steps and how to use them to secure your automated agreement processes.") help page.

## Prerequisites and limitations

The Risk Assessment step is only available to U.S.-based
participants. To add a Risk Assessment step, process builders must meet the
following criteria:

- Their account must enable Risk Assessment
- They must be an account administrator or a user with Workflows:
  Create permissions.

## Risk Assessment step data

If the Risk Assessment step configuration allows data storage,
Workflow Builder generates an ID Evidence file upon completion of the step. To retrieve the
ID Evidence information, process builders must add a Store
files step after the Risk Assessment step.
For more information, read the [ID Evidence in Workflow Builder](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=kmm1749205469137.html&_LANG=enus "Read about ID Evidence integration with Workflow Builder and how it helps deliver evidence of the ID verification process.") page.

## Risk Assessment step vs. Risk-Based Verification

The Risk Assessment step and the ID Verification
Risk-Based Verification (RBV) method allow assessment of
participant risk. However, they both differ in scope and functionality. While
Risk Assessment is a Workflow Builder process step,
Risk-Based Verification is an ID Verification method tied
to an eSignature envelope. Risk Assessment only computes each
participant's risk score. Risk-Based Verification computes a
risk score and triggers a specific ID Verification configuration based on it.

While Risk Assessment does not include identity verification,
process builders can use participants' risk scores to define subsequent workflow
steps, including the Verify Someone's Identity step.

Both the Risk Assessment step and the ID Verification
Risk-Based Verification (RBV) allow storage of
participants' data in ID Evidence.
