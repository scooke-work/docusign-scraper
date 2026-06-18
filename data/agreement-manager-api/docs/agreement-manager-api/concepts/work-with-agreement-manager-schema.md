---
title: Work with the Agreement Manager API schema
source_url: https://developers.docusign.com/docs/agreement-manager-api/concepts/work-with-agreement-manager-schema/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Agreement Manager API
- Agreement Manager API
- Concepts
- Concepts
- Work With Agreement Manager Schema
scraped_at: '2026-06-18T14:17:04Z'
---

# Work with the Agreement Manager API schema

The central component of the Agreement Manager API schema is the `agreement` object, which represents an agreement that Agreement Manager has processed. The API returns general agreement information in response to the [Agreements:getAgreement](https://developers.docusign.com/docs/agreement-manager-api/reference/agreementmanager/agreements/getagreement/) and [Agreements:getAgreementsList](https://developers.docusign.com/docs/agreement-manager-api/reference/agreementmanager/agreements/getagreementslist/) requests.

## Key agreement properties and objects

Several key properties and objects are associated with each `agreement` object. Their relationships are illustrated below, and the next sections provide details. For a complete list of `agreement` properties and objects, see the [API Reference](https://developers.docusign.com/docs/agreement-manager-api/reference/).

![](data:image/svg+xml;charset=utf-8,%3Csvg height='856.9999999999999' width='1147' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Sample agreement and related schema objects](https://images.ctfassets.net/aj9z008chlq0/K274XidrHyDWruWwUFu7r/3a45dff38697435194654431c0963e3a/NavigatorSchema.png?w=1147&h=857&q=50&fm=png)

### Category

An agreement's `category` property reflects a broad classification to which the agreement belongs. Each agreement has one category. The sample agreement shown in the diagram belongs to the business services category. Each agreement category has an associated set of agreement types.

### Type

An agreement's `type` property contains a more specific classification. Each agreement has one type. The diagram shows an agreement whose type is "Statement of Work". The Agreement Manager platform supports a set of [standard agreement types](https://developers.docusign.com/docs/agreement-manager-api/concepts/work-with-agreement-manager-schema/#standard-agreement-types), as well as [custom agreement types](https://developers.docusign.com/docs/agreement-manager-api/concepts/work-with-agreement-manager-schema/#custom-agreement-types).

### Parties

An agreement's `parties` object consists of an array of individuals or entities who participated in the agreement. For example, a lease agreement's parties might consist of a lessor and a lessee. There is no limit on the number of parties to an agreement.

### Provisions

An agreement's `provisions` object contains a list of properties that define the agreement parameters. For example, a statement of work's provisions include properties such as an execution date, a total value, and one or more payment due dates. Each agreement has multiple provisions.

Each agreement type that Agreement Manager supports has a distinct set of provisions that are available with agreements of that type.

A sample `Agreements:getAgreement` response that includes the above components is shown here:

```
{
  "id": "77b85334-xxxx-xxxx-xxxx-f8f029d8c3c5",
  "type": "Statement of Work",
  "category": "BusinessServices",
  "parties": [
    {
      "id": "aba3d8ca-xxxx-xxxx-xxxx-bdab40102a2f",
      "name_in_agreement": "ACME, INC"
    },
    {
      "id": "eb01cef7-xxxx-xxxx-xxxx-3c643357ce18",
      "name_in_agreement": "TALLY, LTD"
    }
  ],
  "provisions": {
    "effective_date": "2024-09-01T00:00:00+02:00",
    "expiration_date": "2029-09-01T00:00:00+02:00",
    "execution_date": "2024-08-15T11:45:00+02:00",
    "total_agreement_value": 150000,
    "total_agreement_value_currency_code": "USD",
    "annual_agreement_value": 50000,
    "annual_agreement_value_currency_code": "USD",
    "term_length": "P3Y",
    "assignment_type": "YES_WITH_CONDITIONS",
    "assignment_change_of_control": "NO_OR_CONSENT_REQUIRED",
    "assignment_termination_rights": "YES",
    "governing_law": "California",
    "jurisdiction": "California",
    "payment_terms_due_date": "THIRTY_DAYS",
    "can_charge_late_payment_fees": true,
    "late_payment_fee_percent": 0,
    "price_cap_percent_increase": 5,
    "liability_cap_fixed_amount": 0,
    "liability_cap_currency_code": "USD",
    "liability_cap_multiplier": 0,
    "liability_cap_duration": "P1Y",
    "renewal_type": "AUTO_RENEW",
    "renewal_notice_period": "P90D",
    "renewal_notice_date": "2024-10-17T14:30:00+02:00",
    "auto_renewal_term_length": "P3Y",
    "renewal_extension_period": "P1Y",
    "renewal_process_owner": "199b3cc9-ec67-47a5-9dff-04ff091d4ca3",
    "renewal_additional_info": "N/A",
    "termination_period_for_cause": "P1Y",
    "termination_period_for_convenience": "P1Y"
  },
  "related_agreement_documents": {
    "parent_agreement_document_id": "f30761c6-xxxx-xxxx-xxxx-e6f3313c95bd"
  },
  "languages": [
    "en-US"
  ],
  "source_name": "Docusign eSign",
  "source_id": "8ade6915-xxxx-xxxx-xxxx-9c6ba6aa1bb5",
  "source_account_id": "3b324aff-xxxx-xxxx-xxxx-0a621c8ac141",
  "metadata": {
    "created_at": "2024-10-01T00:00:00Z",
    "created_by": "a7b0e58b-xxxx-xxxx-xxxx-a7d8790cd571",
    "request_id": "b0f2a7c4-xxxx-xxxx-xxxx-567890123abc",
    "response_timestamp": "2024-10-17T14:30:59Z",
    "response_duration_ms": 110
  }
}
```

## Sources for Agreement Manager API schema values

Agreement Manager populates schema values from two sources. The initial source is the data extraction that the Agreement Manager AI performs to identify agreement parameters, including the agreement type, parties, and provisions. For example, the Agreement Manager AI can use agreement attributes to determine that a value is a renewal type, store it in the appropriate schema field, and return it in the `provisions` object's `renewal_type` property in the response to a Agreement Manager API [Agreements:getAgreement](https://developers.docusign.com/docs/agreement-manager-api/reference/agreementmanager/agreements/getagreement/) request.

Another possible source of Agreement Manager schema values is user input. The Agreement Manager UI enables users to review an agreement's AI-extracted values and add, modify, or delete them. This updates the schema values for the agreement, and any subsequent Agreement Manager API GET requests will return the user-updated values instead of the original AI-extracted values. In a future release, the Agreement Manager API will support the updating of AI-extracted agreement values via API requests.

## Standard agreement types

Below are lists of standard agreement types that the Agreement Manager API supports in the current release. Select a tab to see the agreement types under that category. The agreement type names and category names are listed as they appear in responses to API requests.

- Certificate of Insurance
- Consulting Agreement
- Credit Card Agreement
- Engagement Letter
- Franchise Agreement
- Investment Account Agreement
- Joint Venture Agreement
- Letter of Intent
- Loan agreement
- Marketing agreement
- Master Service Agreement
- Memorandum of Understanding
- Non-disclosure Agreement
- Order Form
- Partnership Agreement
- Proposal agreement
- Purchase Agreement
- Purchase Order
- Quote agreement
- Service Level Agreement
- Services Agreement
- Statement of Work
- Stock Purchase Agreement
- Subscription agreement
- Supply / Distribution agreement
- Wealth Management Agreement

## Custom agreement types

In addition to a set of standard agreement types, the Agreement Manager platform supports the creation of custom agreement types. In the current release, custom agreement types can only include provisions from the standard list of Agreement Manager provisions. Custom provisions will be supported in a future release. See [Create New Agreement Types﻿](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=gke1727282238086.html) for details about creating custom agreement types.

## Next steps

- Review the [How-to guides](https://developers.docusign.com/docs/agreement-manager-api/how-to/) to see sample code that you can use with your integration.
- See the [API Reference](https://developers.docusign.com/docs/agreement-manager-api/reference/) for details about request and response format.

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
