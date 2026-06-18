---
title: Events and alerts
source_url: https://developers.docusign.com/docs/monitor-api/monitor101/events-alerts/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Monitor API
- Monitor API
- API 101
- API 101
- Events and Alerts
scraped_at: '2026-06-18T21:15:04Z'
---

# Events and alerts

Docusign Monitor tracks eSignature and CLM account activity across your organization in near real-time. This activity is made up of *events* resulting from the actions taken by users, administrators, and APIs connected to your organization.

When specific sets of events occur in your organization (typically events that indicate possible suspicious activity), Docusign Monitor can trigger an *alert*. When an alert is triggered, the activity that caused the alert is recorded in Monitor or your SIEM system, and the appropriate administrator or security operations team member is automatically notified.

Monitor includes alerts for common types of suspicious activity—such as a user deleting a large number of envelopes in a short period of time, or removing a signer authentication requirement. Security teams can also leverage the Monitor API and their existing security stack to create custom alerts that meet their organization and regulatory requirements.

See [Monitor event properties](https://support.docusign.com/s/document-item?bundleId=gso1581445176035&topicId=lcd1585600758257.html) for details on the properties of a monitor event.

## List of tracked events

**eSignature**See [Docusign Monitor eSignature events](https://support.docusign.com/s/document-item?bundleId=gso1581445176035&topicId=crj1659119600990.html) for a summary list of all eSignature events. **CLM**

See [Docusign Monitor CLM events](https://support.docusign.com/s/document-item?bundleId=gso1581445176035&topicId=refccb593b2-ea43-40d9-93bd-5655e2162e5c.html) for a summary of list of all CLM events.

**Maestro Workflows**See [Docusign Monitor Maestro events](https://support.docusign.com/s/document-item?bundleId=gso1581445176035&topicId=refb31b2b17-00f6-4fdc-8b27-9003442f4b2e.html) for a summary of list of all Maestro events. **Navigator**See [Docusign Monitor Navigator events](https://support.docusign.com/s/document-item?bundleId=gso1581445176035&topicId=ref427e7726-6e39-4fa2-9d3b-6f6abdfb0698.html) for a summary of list of all Navigator events

## List of tracked alerts

See [Docusign Monitor eSignature alerts](https://support.docusign.com/s/document-item?bundleId=gso1581445176035&topicId=refd45c3b91-27da-49ee-aba6-f946c7e203da.html) for details on eSignature alerts, and [Docusign Monitor CLM alerts](https://support.docusign.com/s/document-item?bundleId=gso1581445176035&topicId=refd432e355-b91a-47ae-b979-1f263d4fe154.html) for details on CLM alerts.

See [Docusign Monitor Maestro alerts](https://support.docusign.com/s/document-item?bundleId=gso1581445176035&topicId=refabf22c9d-dafd-45ba-96b8-5e7053517a27.html) for details on Maestro alerts, and [Docusign Monitor Navigator alerts](https://support.docusign.com/s/document-item?bundleId=gso1581445176035&topicId=refeb6cc0d4-f4b8-4c35-88af-0573e1b13277.html) for details on Navigator alerts.

## Next steps

- See [Docusign Monitor eSignature events](https://support.docusign.com/s/document-item?bundleId=gso1581445176035&topicId=crj1659119600990.html) for a summary list of all eSignature events.
- See [Docusign Monitor eSignature alerts](https://support.docusign.com/s/document-item?bundleId=gso1581445176035&topicId=refd45c3b91-27da-49ee-aba6-f946c7e203da.html) for details on eSignature alerts, and [Docusign Monitor CLM alerts](https://support.docusign.com/s/document-item?bundleId=gso1581445176035&topicId=refd432e355-b91a-47ae-b979-1f263d4fe154.html) for details on CLM alerts.
- See details about the Event and Alert objects in the [API Reference](https://developers.docusign.com/docs/monitor-api/reference/).

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
