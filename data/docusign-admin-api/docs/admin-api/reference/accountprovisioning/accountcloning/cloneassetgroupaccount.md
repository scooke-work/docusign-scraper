---
title: ': cloneAssetGroupAccount'
source_url: https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/
site: developers.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T20:12:06Z'
---

[API Reference](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/)[API Explorer](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/?explorer=true)

[AccountCloning](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/)

# : cloneAssetGroupAccount

Clones an existing Docusign account. Cloning an account copies the plan items and eSignature settings. Users, templates, and permission profiles are *not* copied into the target account. The new account will linked to the same organization.

In the request body, specify the source account you are cloning by its ID. You can get the IDs for your organization's asset group accounts using the [getAssetGroupAccounts](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/getassetgroupaccounts/) endpoint.

You also need to specify information about the new target account, including the name, location, and administrator. To set the location, provide either the `countryCode` or `region` properties. (If both are specified, the `region` value will be used.) When testing in the developer environment, the region will always be `NA`.

The request body looks like this:

```
{
    "sourceAccount": {
        "id": "624e3e00-xxxx-xxxx-xxxx-43918c520dab"
    },
    "targetAccount": {
        "name": "My Cloned Account",
        "admin": {
            "firstName": "Francis",
            "lastName": "Beagle",
            "email": "francis@example.com"
        },
        "region": "NA"
    }
}
```

To call this endpoint:

- You must be an administrator for the specified organization. The administrator for the target account must also be an organization admin.
- The source account must be on the same plan as your contract.
- The source account must be an asset group account. An asset group is a set of modules, products, plans, and charges purchased for your organization. An asset group account is an account that has been linked to an asset group.
- Your organization must be set up for account cloning. For more information, email [self-serve-provisioning-enablement@docusign.com](mailto:self-serve-provisioning-enablement@docusign.com).

[Required scopes](https://developers.docusign.com/docs/admin-api/admin101/auth/): `asset_group_account_clone_write`.

### Next steps

- See [how to use this endpoint to clone an account](https://developers.docusign.com/docs/admin-api/how-to/clone-account/).

## Request

#### HTTP Request

POST

```
/Management/v2/organizations/{organizationId}/assetGroups/accountClone
```

## Parameters

| Path Parameters |  |  |
| --- | --- | --- |
| organizationId \* | string | The organization's GUID. |

\* Required

## SDK Method

### AccountProvisioning::cloneAssetGroupAccount

## Request Body

## Responses

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
