---
title: ': getWorkflowTriggerRequirements'
source_url: https://developers.docusign.com/docs/workflow-builder-api/reference/workflowbuilder/workflows/getworkflowtriggerrequirements/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Workflow Builder API
- Workflow Builder API
- API Reference
- API Reference
- Workflowbuilder
- Workflowbuilder
- Workflows
- Workflows
- Getworkflowtriggerrequirements
scraped_at: '2026-06-18T17:59:19Z'
---

[Workflows](https://developers.docusign.com/docs/workflow-builder-api/reference/workflowbuilder/workflows/)

# : getWorkflowTriggerRequirements

This operation retrieves the configuration and input requirements necessary to trigger a specific
Workflow Builder workflow. It provides detailed information about the `trigger_event_type`, such as HTTP
or other supported types, and specifies the required input schema, including field names, data types,
and any default values.

This information is essential for understanding the data and parameters required to initiate the
workflow. It enables developers to prepare the necessary inputs and configuration before triggering
the workflow instance, ensuring seamless execution and compliance with workflow requirements.

### Use Cases:

- Identifying the required input fields and their data types to successfully trigger the workflow.
- Reviewing the trigger configuration for validation and compliance with expected input.
- Preparing and validating data in advance of triggering the workflow, minimizing runtime errors.

### Key Features:

- **Detailed Trigger Input Requirements**: Provides an exhaustive schema of required fields,
  their data types, and optional default values for easy reference and data validation.
- **Trigger Event Type Information**: Specifies the type of event required to initiate the workflow
  (e.g., HTTP), helping developers configure their systems to invoke the workflow appropriately.
- **Configurable for Custom Triggers**: Suitable for custom configurations, enabling flexibility
  in how workflows can be triggered according to system needs.

HTTP Request

GET

```
/v1/accounts/{accountId}/workflows/{workflowId}/trigger-requirements
```

Base URL : Demo

```
https://api-d.docusign.com
```

## Request

Path Parameters

workflowId

---

WorkflowId

Use example values

adf8c455-de2f-4119-b183-d952d649e87c

\*required

A universally unique identifier (UUID) in standard 8-4-4-4-12 format.

pattern: ^[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?$

## Response

###### Request Example

1

2

3

curl --location "https://

api-d.docusign.com/

v1/accounts/

{accountId}/

workflows/

{workflowId}/

trigger-requirements"

--header "Authorization:

Bearer {accessToken}"

--header "Content-Type:

application/json"

Was this result helpful?

###### Response Example

JSON

Click Try It! to start a request and see the response here!

Or choose an example:

Was this result helpful?

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
