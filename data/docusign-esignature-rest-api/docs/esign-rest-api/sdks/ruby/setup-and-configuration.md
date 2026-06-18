---
title: Ruby SDK setup and configuration
source_url: https://developers.docusign.com/docs/esign-rest-api/sdks/ruby/setup-and-configuration/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- SDKs
- SDKs
- Ruby
- Ruby
- Setup and configuration
scraped_at: '2026-06-18T21:09:55Z'
---

# Ruby SDK setup and configuration

## Adding the SDK to your project

The Ruby SDK is provided as a gem named
[docusign\_esign](https://rubygems.org/gems/docusign_esign/). By default, you will always get the latest stable version of the SDK. Prerelease versions (either release candidate (rc) or beta) can also be downloaded, as shown below.

There are three ways to add the package to your project: via your project’s Gemfile, your preferred console, or by downloading the SDK from GitHub.

### Adding the Ruby SDK to your project using your project’s Gemfile

1. In your application's Gemfile, add:
   `gem 'docusign_esign'`
2. Open your console, navigate to your project directory, and run:
   `bundle install`

If desired, you can specify a version. For example, adding the following to your project’s Gemfile installs version 3.5.0 of the Docusign Ruby eSignature gem:

```
    gem 'docusign_esign', '~> 3.5'
```

### Adding the Ruby SDK to your project using your console

1. In your console, run:
   `gem install docusign_esign`

To specify a version using your console, you can use the -v switch as in the following example:

```
    gem install docusign_esign -v 3.5.0
```

### Downloading the SDK from the GitHub repository

This open-source SDK is available for download in cases where you would like to make changes to the SDK. You can download the SDK from GitHub using the instructions below:

1. Download or clone the SDK from the
   [docusign-esign-ruby-client](https://github.com/docusign/docusign-ruby-client) repository.
2. In the console, navigate to local\_path\_to\_repo/docusign-esign-ruby-client and run the following command:

   ```
       gem build docusign_esign.gemspec
   ```
3. Install the gem from the newly generated gem file. For example:

   ```
       gem install docusign_esign-3.9.0.gem
   ```

You can also select a different version to download from the
[docusign-esign-ruby-client](https://github.com/docusign/docusign-ruby-client) repository's
[release history](https://github.com/docusign/docusign-ruby-client/releases).

## Including the SDK library

Once you have installed the docusign\_esign gem, you need to find the public classes that are required to complete various eSignature tasks. When developing with Ruby on Rails and Bundler, the following line in config/application.rb takes care of requiring all the gems specified in your Gemfile:

```
    Bundler.require(*Rails.groups)
```

When using RubyGems by itself, you must add the following
`require` statement in your Ruby code:

```
    require 'docusign_esign'
```

To access Docusign eSignature public classes and methods in your code, use the namespace
`Docusign_eSign`.

### [Docusign eSignature API classes](https://github.com/docusign/docusign-ruby-client/tree/master/lib/docusign_esign/api)

These Ruby SDK classes contain endpoint categories. Each of these classes corresponds to one of the categories listed in the left menu of the
[eSignature REST API reference](https://developers.docusign.com/docs/esign-rest-api/reference/). You will need these classes to make calls to the SDK methods that initiate REST API calls to the Docusign eSignature REST API.

**Note:** Hereafter in the SDK documentation, the term “API object” will refer to
[eSignature REST API reference](https://developers.docusign.com/docs/esign-rest-api/reference/) objects.

An
[API category](https://developers.docusign.com/docs/esign-rest-api/reference/) contains all of the methods for each API resource in that category. For example, the Ruby SDK
`EnvelopesApi` class includes the
`create_envelope` method. This method corresponds to the API Envelopes resource
[create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) method.

The SDK’s method names roughly correspond to the API Resource:method names.

The API Reference page for each endpoint lists the corresponding SDK method associated with that endpoint. To find the Ruby SDK method that corresponds to an API Resource:method page, use the API Reference page’s
**SDK Method** box. The Ruby method name will be the “snake\_case” version of the API SDK method name. For example, the API SDK Method
`Envelopes::createEnvelope` is the Ruby SDK method
`create_envelope`.

### [Docusign eSignature Model classes](https://github.com/docusign/docusign-ruby-client/tree/master/lib/docusign_esign/models)

These classes contain the objects used for sending and receiving data from the eSignature API endpoints. By using these classes instead of generic JSON objects, Ruby developers can develop with the Docusign eSignature API more easily and quickly than by using JSON directly.

There’s a one-to-one correspondence between the objects described in the
[API Reference](https://developers.docusign.com/docs/esign-rest-api/reference/) and the classes in the Ruby Docusign eSignature Model classes. The API object names use camelCase (the first letter is lowercase) while the corresponding SDK models use PascalCase (the first letter is uppercase). For example, the API object
[paymentgatewayaccount](https://developers.docusign.com/docs/esign-rest-api/reference/payments/paymentgatewayaccounts/list/#response200_paymentgatewayaccount) corresponds to the Ruby object
[PaymentGatewayAccount](https://github.com/docusign/docusign-ruby-client/blob/master/lib/docusign_esign/models/payment_gateway_account.rb).

**Note:** The API object name is often not the same as the corresponding model in the Ruby SDK.

Object attribute names in the API also use camelCase. The corresponding properties of the Ruby SDK are in “snake\_case.”

Some API endpoints also use HTTP query parameters. Within the API, such query parameters use “snake\_case.” For example, the
[Envelopes:create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) API method includes an optional query parameter,
`change_routing_order`. Within the SDK, the API’s query parameters are added as an elective
`options` parameter after the request object.

**Example:** The
`Docusign_eSign::EnvelopesApi.create_envelope` method signature is:

```
    def create_envelope(account_id, envelope_definition, options = Docusign_eSign::CreateEnvelopeOptions.default)
```

The
`CreateEnvelopeOptions` class is used to set the API method’s query parameters. The class is defined as:

```
      class CreateEnvelopeOptions
        attr_accessor :cdse_mode
        attr_accessor :change_routing_order
        attr_accessor :completed_documents_only
        attr_accessor :merge_roles_on_draft
        attr_accessor :tab_label_exact_matches

        def self.default
          @@default ||= CreateEnvelopeOptions.new
        end
      end
```

The class attributes in "snake\_case" correspond to the API endpoint's query parameters.

### [Docusign eSignature Client, OAuth, and ApiError classes](https://github.com/docusign/docusign-ruby-client/tree/master/lib/docusign_esign/client)

These classes are needed to manage the overall API experience. The
`Client`,
`OAuth`, and
`ApiError` classes, respectively, handle instantiating a client element to make API calls, authenticating, and exception handling. You will need these classes to be able to use the Docusign eSignature API correctly.

### Using the SDK

To make eSignature REST API calls with the SDK, you need:

- A current access token
- The base path for the API call
- For most API calls, you’ll also need the relevant
  `account_id`. Note that it is common for a user to be a member of multiple accounts.

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
