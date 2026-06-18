---
title: PHP SDK setup and configuration
source_url: https://developers.docusign.com/docs/esign-rest-api/sdks/php/setup-and-configuration/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- SDKs
- SDKs
- PHP
- PHP
- Setup and configuration
scraped_at: '2026-06-18T20:28:15Z'
---

# PHP SDK setup and configuration

Learn about [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/) and how you can use it to quickly set up and run eSignature REST API code examples.

## Adding the SDK to your project

The PHP eSignature SDK is provided as a Composer package named [docusign/esign-client](https://packagist.org/packages/docusign/esign-client/). By default, you will always get the latest stable version of the SDK. Prerelease versions (either release candidate (RC) or beta) can also be downloaded, as shown below.

There are two ways to add the package to your project: via the command line or by downloading the SDK from GitHub.

### Adding the SDK to your project using the command line

1. From the command line, run: `composer require docusign/esign-client`
2. To use the package automatically, add to Composer's `Autoload` file: `require_once('vendor/autoload.php');`

### Downloading the SDK from the GitHub repository

This open-source SDK is available for download in cases where you would like to make changes to the SDK. You can download the SDK from GitHub using the instructions below:

1. Download or clone the SDK from the [docusign-esign-php-client](https://github.com/docusign/docusign-esign-php-client) repository.
2. Bind the PHP SDK to your server or place it in a static location.
   - To bind to your server, in your init.php file, add: `require_once('/path/to/docusign-esign-client/autoload.php');`
   - To bind to single files, in your PHP file that will utilize the PHP SDK, add: `require_once('/path/to/docusign-esign-client/autoload.php');`

Note: If you are using Composer V2 and get the error `namespace cannot be found`, add the following class mapping in the composer.json file:

 `"autoload": { "classmap": [ "/path/to/docusign-esign-client/src" ] }`Both of the methods listed above will automatically install the latest stable version. If desired, you can specify a version. For example, you can specify version 6.0.0 of the PHP SDK by doing the following:

1. Update the entry for the SDK in the `require` section of your project’s composer.json file: `"docusign/esign-client": "^6.0.0",`
2. From the command line, run: `composer update`

## Including the SDK library

Once you have added the PHP SDK to your project, you will need to access the public classes that you will use. These are the principal top-level namespaces in the PHP eSignature SDK:

- [Docusign\eSign\Api](https://developers.docusign.com/docs/esign-rest-api/sdks/php/setup-and-configuration/#docusign-esign-api-classes)
- [Docusign\eSign\Model](https://developers.docusign.com/docs/esign-rest-api/sdks/php/setup-and-configuration/#docusign-esign-model-classes)
- [Docusign\eSign\Client](https://developers.docusign.com/docs/esign-rest-api/sdks/php/setup-and-configuration/#docusign-esign-client-classes)

## Docusign\eSign\Api classes

These [PHP SDK classes](https://github.com/docusign/docusign-esign-php-client/tree/master/src/Api) contain endpoint categories. Each of these classes corresponds to one of the categories listed in the left menu of the [eSignature REST API](https://developers.docusign.com/docs/esign-rest-api/) reference. You will need to use these classes to make calls to the public methods that initiate REST API calls to the eSignature REST API.

**Note**: Hereafter in the SDK documentation, the term “API object” will refer to [eSignature REST API](https://developers.docusign.com/docs/esign-rest-api/) reference objects.

An [API category](https://developers.docusign.com/docs/esign-rest-api/reference/) contains all of the methods for each API resource in that category. For example, the PHP SDK [EnvelopesApi](https://github.com/docusign/docusign-esign-php-client/blob/master/src/Api/EnvelopesApi.php) class includes the [createEnvelope](https://github.com/docusign/docusign-esign-php-client/blob/master/src/Api/EnvelopesApi.php#L4686) method. This method corresponds to the [Envelopes:create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) method of the API [Envelopes](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/) resource.

The SDK’s method names roughly correspond to the API Resource: method names. The API Reference page for each endpoint lists the corresponding SDK method associated with that endpoint.

To find the PHP SDK method that corresponds to an API Resource:method page, use the API Reference page’s **SDK Method** box. The PHP method name will roughly correspond to the API’s SDK Method. For example, the API SDK Method `Envelopes::createEnvelope` is the PHP SDK method [createEnvelope](https://github.com/docusign/docusign-esign-php-client/blob/master/src/Api/EnvelopesApi.php#L4686).

## Docusign\eSign\Model classes

This [namespace](https://github.com/docusign/docusign-esign-php-client/tree/master/src/Model) contains data structures and methods used to send and receive data from the eSignature API endpoints. By using these classes instead of generic JSON objects, we make PHP development with the eSignature API easier and faster than using JSON directly.

There’s a one-to-one correspondence between the objects described in the [API Reference](https://developers.docusign.com/docs/esign-rest-api/reference/) and the classes in the `Docusign\eSign\Model` namespace. The API object names use camelCase (the first letter is lowercase) while the corresponding SDK models use PascalCase (the first letter is uppercase). For example, the API object [paymentGatewayAccounts](https://developers.docusign.com/docs/esign-rest-api/reference/payments/paymentgatewayaccounts/list/#definition_200_paymentgatewayaccountsinfo_paymentgatewayaccountsinfo_paymentgatewayaccounts) corresponds to the PHP object [PaymentGatewayAccount](https://github.com/docusign/docusign-esign-php-client/blob/master/src/Model/PaymentGatewayAccount.php#L46).

Note: The API object name is not necessarily the same as the corresponding model in the PHP SDK.

Object attribute names in the API also use camelCase. The corresponding properties of the PHP SDK are in PascalCase.

Some API endpoints also use HTTP query parameters. Within the API, the query parameters use "snake\_case." For example, the [Envelopes:create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) API method includes an optional query parameter, `change_routing_order`. Within the SDK, the API’s query parameters are added as an elective `options` parameter after the request object.

**Example:** The [createEnvelope](https://github.com/docusign/docusign-esign-php-client/blob/master/src/Api/EnvelopesApi.php#L4686) method signature is:

```
  public function createEnvelope($account_id, $envelope_definition = null, \Docusign\eSign\Api\EnvelopesApi\CreateEnvelopeOptions $options = null)
```

The [CreateEnvelopeOptions](https://github.com/docusign/docusign-esign-php-client/blob/master/src/Api/EnvelopesApi.php#L127) class is used to set the API method’s query parameters. The class is defined as:

```
class CreateEnvelopeOptions
    {
        public function getCdseMode(): string
        public function setCdseMode(string $cdse_mode): self
        public function getChangeRoutingOrder(): string
        public function setChangeRoutingOrder(string $change_routing_order): self
        public function getCompletedDocumentsOnly(): string
        public function setCompletedDocumentsOnly(string $completed_documents_only): self
        public function getMergeRolesOnDraft(): string
        public function setMergeRolesOnDraft(string $merge_roles_on_draft): self
        public function getTabLabelExactMatches(): string
        public function setTabLabelExactMatches(string $tab_label_exact_matches): self
    }
```

The class attributes in camelCase correspond to the API endpoint’s query parameters. The `cdse_mode` and `completed_documents_only` parameters are reserved for Docusign internal use only. More details can be found on the Query parameters section within our [API reference for the createEnvelopes method](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/). The other methods `change_routing_order` and `merge_roles_on_draft` take boolean strings ("true" or "false") and can be configured as such:

```
    $config = new  \Docusign\eSign\Configuration();
    $config->setHost($args['base_path']);
    $config->addDefaultHeader('Authorization', 'Bearer ' . $args['ds_access_token']);

    $apiClient = new \Docusign\eSign\Client\ApiClient($config);
    $envelope_api = new \Docusign\eSign\Api\EnvelopesApi($apiClient);

    $options = new \Docusign\eSign\Api\EnvelopesApi\CreateEnvelopeOptions();
    $options->setMergeRolesOnDraft("true");
    $options->setChangeRoutingOrder("true");

    $envelopeSummary = $envelope_api->createEnvelope($args['account_id'], $envelope_definition, $options);
```

## Docusign\eSign\Client classes

This [namespace](https://github.com/docusign/docusign-esign-php-client/tree/master/src/Client) contains the classes needed to manage the overall API experience. These include the classes needed to instantiate a client element to make API calls and the classes used for authentication and exception handling. You will need to include this namespace to be able to use the Docusign eSignature API correctly.

## Using the SDK

To make eSignature REST API calls with the SDK, you will need:

- A current access token.
- The base path for the API call.
- For most API calls, you’ll also need the relevant `account_id`. Note that it is common for a user to be a member of multiple accounts.

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
