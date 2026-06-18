---
title: Enable ID Evidence storage
source_url: https://developers.docusign.com/docs/idevidence-api/idevidence101/enabling-idevidence-storage/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- ID Evidence API
- ID Evidence API
- API 101
- API 101
- Enable ID Evidence Storage
scraped_at: '2026-06-18T21:43:33Z'
---

# Enable ID Evidence storage

To store images of the government-issued IDs captured by the ID verification (IDV) process for each signer, you must have the **Front side of the ID** and **Back side of the ID** options selected.

## Verify and edit your IDV configuration

1. In Docusign eSignature Settings, select **Identity Verification**.
   1. If you do not see a sidebar link named **Identity Verification** under eSignature Settings in your Docusign account, you do not have ID Verification (IDV) enabled. See [ID verification](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/auth/#idv) for information on enabling IDV in your account.
2. Locate your **Docusign ID Verification** configuration from the list.
   1. If your **Docusign ID Verification** configuration has **Read-only** permission, [create a new IDV configuration](https://developers.docusign.com/docs/idevidence-api/idevidence101/enabling-idevidence-storage/#create-a-new-idv-configuration).
3. Select **ACTIONS** for the IDV configuration you want to edit and select **Edit**.
4. Under the **Data to save from each Photo ID or Passport verification** section, make sure  that **Front side of the ID** and **Back side of the ID** are selected as shown in the image.
   1. If they are not selected, select the two boxes as per the image.
5. Select **SAVE**.

## Create a new IDV configuration

1. In Docusign eSignature Settings, select **Identity Verification**.
2. Select **ADD CONFIGURATION**.
3. Enter a name (and optional description) for the configuration.
4. For the verification method, select **Docusign ID Verification** from the dropdown menu.
5. Under the **Data to save from each Photo ID or Passport verification** section, select **Front side of the ID** and **Back side of the ID** as shown in the image.
6. Select **SAVE**.
7. [Add your new IDV configuration to a recipient](https://developers.docusign.com/docs/idevidence-api/idevidence101/enabling-idevidence-storage/#add-your-new-idv-configuration-to-a-recipient).

## Add your new IDV configuration to a recipient

1. Start a new envelope and add documents and recipients as usual.
2. For the recipient for whom you want to request identity verification, select **CUSTOMIZE** then select **Add identity verification**.
3. Select your new IDV configuration from the list of **Identity Verification** methods.
4. Finish preparing your envelope as usual and send it.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1329' width='2604' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Make sure both "Front side of the ID" and "Back side of the ID" are selected.](https://images.ctfassets.net/aj9z008chlq0/A7QofG3EtCR4HzqKLajAo/9d0b1dc9f70378b20c7e247a2e8375d4/IDV_better.png?w=2604&h=1329&q=50&fm=png)

## Next steps

- See the Support article [Add Identity Verification Configurations﻿](https://support.docusign.com/s/document-item?rsc_301&bundleId=pik1583277475390&topicId=dnh1583277456343.html) for details about creating IDV configurations.
- See the Support article [To add ID verification for a recipient](https://support.docusign.com/s/document-item?language=rsc_301&bundleId=ced1643229641057&topicId=whh1578456529441.html) for more information.

[![Footer: Platform 101: Pre-Footer - Icon](https://images.ctfassets.net/aj9z008chlq0/1B2IgSQD94ohLe7UVvJ5AU/ef33d80a2fbfcf734362995ffd43a438/footer-icon-1.svg)

Platform 101

Get up to speed on our concepts and platform](https://developers.docusign.com/platform/build-integration/)[Learn More](https://developers.docusign.com/platform/build-integration/)[![Footer: Stack Overflow: Pre-Footer - Icon](https://images.ctfassets.net/aj9z008chlq0/4gZwid50MSnlXqHMTZLCdV/4cc92d22086124f2f622c781cb554844/footer-icon-2.svg)

Docusign Community

Get answers from our API experts and community](https://community.docusign.com/developer-59)[Learn More](https://community.docusign.com/developer-59)[![Footer: GitHub: Pre-Footer - Icon](https://images.ctfassets.net/aj9z008chlq0/208FBzUKngjwdVfL0wAgd7/f6ff4fd8071196e37c5cac5f4f12c38c/footer-icon-3.svg)

GitHub

Find our SDKs and other source code](https://github.com/docusign)[Learn More](https://github.com/docusign)[![Footer: Partner Directory: Pre-Footer - Icon](https://images.ctfassets.net/aj9z008chlq0/2YWAk0yl09YARzBDgoq6dN/48d159475098419d1da9b3fcf14a4791/footer-icon-4.svg)

Partner Directory

See the full directory of Docusign partners](https://partners.docusign.com/s/partnerfinder)[Learn More](https://partners.docusign.com/s/partnerfinder)

[![Docusign.com](https://developers.docusign.com/img/docusign-logo.svg)](https://docusign.com)

[![X](https://images.ctfassets.net/aj9z008chlq0/jUnMYaPzapgZma42YHdEv/375916f63ce5f10c79da650018f8cb0c/x-logo.png)](https://x.com/DocusignDevs)[![youtube](https://images.ctfassets.net/aj9z008chlq0/pYBeoyZ3yAWrQ7yx2MV6U/c3e2679fb091dd6f6dbf9b250bd5ed9a/social-icon-youtube.png)](https://www.youtube.com/@DocusignDevs)[![linkedin](https://images.ctfassets.net/aj9z008chlq0/5dZh3hbAdZ97DYDNdhijTA/19230fd1c70b76dea1eef8834779e2cd/social-icon-linkedin.png)](https://www.linkedin.com/showcase/docusigndevs/)

APIs- [eSignature API](https://developers.docusign.com/docs/esign-rest-api/)
- [Web Forms API](https://developers.docusign.com/docs/web-forms-api/)
- [Workflow Builder API](https://developers.docusign.com/docs/workflow-builder-api/)
- [Agreement Manager API](https://developers.docusign.com/docs/agreement-manager-api/)
- [Docusign Admin API](https://developers.docusign.com/docs/admin-api/)
- [View all](https://developers.docusign.com/docs/)

Featured Content- [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/)
- [Sample Apps](https://developers.docusign.com/sample-apps/)
- [Authentication](https://developers.docusign.com/platform/auth/)
- [Webhooks](https://developers.docusign.com/platform/webhooks/)
- [Go-Live](https://developers.docusign.com/platform/go-live/)
- [SDKs](https://developers.docusign.com/docs/sdks/)

Help- [Support](https://developers.docusign.com/support/)
- [FAQs](https://support.docusign.com/s/articles/DocuSign-Developer-Support-FAQs)

More- [Partner With Us](https://developers.docusign.com/partner/)
- [Docusign University](https://developers.docusign.com/training/)
- [Trust Center](https://www.docusign.com/trust)
- [Trust Portal](https://www.docusign.com/trust-portal)
- [ISV integration guides](https://developers.docusign.com/partner/isv-integration-guides/)

[![X](https://images.ctfassets.net/aj9z008chlq0/jUnMYaPzapgZma42YHdEv/375916f63ce5f10c79da650018f8cb0c/x-logo.png)](https://x.com/DocusignDevs)[![youtube](https://images.ctfassets.net/aj9z008chlq0/pYBeoyZ3yAWrQ7yx2MV6U/c3e2679fb091dd6f6dbf9b250bd5ed9a/social-icon-youtube.png)](https://www.youtube.com/@DocusignDevs)[![linkedin](https://images.ctfassets.net/aj9z008chlq0/5dZh3hbAdZ97DYDNdhijTA/19230fd1c70b76dea1eef8834779e2cd/social-icon-linkedin.png)](https://www.linkedin.com/showcase/docusigndevs/)

© 2024 Docusign, Inc.

[Docusign.com](https://docusign.com)

[Terms of Use](https://www.docusign.com/company/terms-and-conditions/developers)

[Privacy Notice](https://www.docusign.com/company/privacy-policy)

[Notice to California Residents](https://www.docusign.com/privacy#8)

[Intellectual Property](https://www.docusign.com/IP)

![ccpa-opt-out](https://developers.docusign.com/img/svg/ccpa-opt-out.svg)
