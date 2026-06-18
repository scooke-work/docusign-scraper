---
title: Java SDK setup and configuration
source_url: https://developers.docusign.com/docs/esign-rest-api/sdks/java/setup-and-configuration/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- SDKs
- SDKs
- Java
- Java
- Setup and configuration
scraped_at: '2026-06-18T21:09:54Z'
---

# Java SDK setup and configuration

Learn about [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/) and how you can use it to quickly set up and run eSignature REST API code examples.

## Adding the SDK to your project

The [Java SDK](https://developers.docusign.com/docs/esign-rest-api/sdks/java/) is provided by Docusign as a Maven package named [docusign-esign-java](https://central.sonatype.com/artifact/com.docusign/docusign-esign-java?smo=true). By default, you will always be shown the latest release candidate (RC) version of the SDK first.

There are several ways to add the package to your Java project using Maven. The two most popular methods are: via the Eclipse user interface or via the command line.

### Adding the Java SDK to your project using the Eclipse UI

1. Open Eclipse and the workspace you wish to use.
2. In your project, double-click the pom.xml file.
3. Edit your pom.xml file to include the `<dependencies></dependencies>` tag, just inside the closing `</project>` tag. When you're finished, it should look like this:

![pom.xml before dependencies](https://developers.docusign.com/img/javasdk_pom1.png?v=20260610.1 "pom.xml before dependencies")

4. Next, copy and paste the Apache Maven XML that references your desired Java eSignature SDK version, as listed on [Maven Central](https://central.sonatype.com/artifact/com.docusign/docusign-esign-java?smo=true). The figure below shows the result:

![pom.xml after dependencies](https://developers.docusign.com/img/javasdk_pom2.png?v=20260610.1 "pom.xml after dependencies")

5. Save the changes to your pom.xml file.
6. Right-click pom.xml and select **Maven > Update Project** to download and compile the Docusign Java eSignature SDK and its dependencies:

![pom.xml update dependencies](https://developers.docusign.com/img/javasdk_pom3.png?v=20260610.1 "pom.xml update dependencies")

You have now successfully downloaded, configured, and installed the Docusign Java eSignature SDK for your project. To confirm the package is available in your project, go to the **Package Explorer** panel and expand  **Maven Dependencies**. You should see **docusign-esign-java-{*version number*}.jar**:

![maven downloaded dependencies](https://developers.docusign.com/img/javasdk_pom4.png?v=20260610.1 "maven downloaded dependencies")

### Adding the Java SDK to your project using the command line

1. Edit your pom.xml file to include the `<dependencies></dependencies>` tag, just inside the closing `</project>` tag.
2. Next, copy and paste the Apache Maven XML that references your desired Java eSignature SDK version, as listed on [Maven Central](https://central.sonatype.com/artifact/com.docusign/docusign-esign-java?smo=true):

![specify pom dependency](https://developers.docusign.com/img/javasdk_cli1.jpg?v=20260610.1 "specify pom dependency")

3. To install the Java eSignature SDK version and its dependencies, in your console, navigate to your project directory, and run: `mvn clean package`

![running mvn clean package](https://developers.docusign.com/img/javasdk_cli2.png?v=20260610.1 "running mvn clean package")

## Including the SDK library

Once the Maven package has been added to the project, you need to find the public classes required to complete various eSignature tasks. To do that, add the main namespaces as `import` statements in your Java code.

Here are some commonly used `import` statements for required namespaces when using the Docusign eSignature SDK.

```
    import com.docusign.esign.client.ApiClient;
    import com.docusign.esign.client.ApiException;
    import com.docusign.esign.api.*;
    import com.docusign.esign.model.*;
```

### [com.docusign.esign.api](https://github.com/docusign/docusign-esign-java-client/tree/master/src/main/java/com/docusign/esign/api) namespace

This namespace is used for endpoint categories. Each class under this namespace corresponds to one of the categories listed in the left menu of the [Docusign eSignature REST API Reference](https://developers.docusign.com/docs/esign-rest-api/reference/). You will need to use this namespace to make calls to the public methods that initiate REST API calls to the Docusign eSignature REST API.

For example, to use the Envelopes API, you would specify:

```
    import com.docusign.esign.api.EnvelopesApi;
```

**Note**: Hereafter in the Java SDK documentation, the term “API object” will refer to [eSignature REST API Reference](https://developers.docusign.com/docs/esign-rest-api/reference/) objects.

An [API category](https://developers.docusign.com/docs/esign-rest-api/reference/) contains all of the methods for each API resource in that category. For example, the Java SDK `EnvelopesApi`class includes the `createEnvelope` method. This method corresponds to the API `Envelopes` resource [create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) method.

The SDK’s method names roughly correspond to the API Resource:method names. The API Reference page for each endpoint lists the corresponding SDK method associated with that endpoint.

To find the Java SDK method that corresponds to an API Resource:method page, use the API Reference page’s **SDK Method** box. The Java method name will be the camelCase version of the API SDK method name. For example, the API SDK Method `Envelopes::createEnvelope` is the Java SDK method `createEnvelope`.

### [com.docusign.esign.model](https://github.com/docusign/docusign-esign-java-client/tree/master/src/main/java/com/docusign/esign/model) namespace

This namespace includes the data structures used for sending and receiving data from the eSignature API endpoints. By using these classes instead of generic JSON objects, Java developers can more easily harness the Docusign eSignature API and spend less time configuring the attributes and type requirements for any API object. To make use of a given API model, specify its name at the end of a model import statement.

For example, if you wish to [send an envelope with recipient phone authentication](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/eSignature/examples/EG020ControllerPhoneAuthentication.java#L14), you would import the following models:

```
    import com.docusign.esign.model.Document;
    import com.docusign.esign.model.EnvelopeDefinition;
    import com.docusign.esign.model.EnvelopeSummary;
    import com.docusign.esign.model.RecipientPhoneAuthentication;
    import com.docusign.esign.model.Recipients;
    import com.docusign.esign.model.SignHere;
    import com.docusign.esign.model.Signer;
```

There’s a one-to-one correspondence between the objects described in the [API Reference](https://developers.docusign.com/docs/esign-rest-api/reference/) and the classes in the com.docusign.esign.model namespace. The API object names use camelCase (the first letter is lowercase) while the corresponding Java SDK model classes use PascalCase (the first letter is uppercase). For example, the API object [paymentgatewayaccount](https://developers.docusign.com/docs/esign-rest-api/reference/payments/paymentgatewayaccounts/list/#response200_paymentgatewayaccount) corresponds to the Java model class [PaymentGatewayAccount](https://github.com/docusign/docusign-java-client/blob/master/src/main/java/com/docusign/esign/model/PaymentGatewayAccount.java).

Object attribute names in the API use camelCase. The corresponding class fields of the Java SDK are also camelCase.

Some API endpoints also use HTTP query parameters. Within the API, such query parameters use “snake\_case.” For example, the `Envelopes:create` API method includes an optional query parameter `change_routing_order`. Within the SDK, the API’s query parameters are added as an elective `options` parameter after the request object.

**Example:** The `EnvelopesApi.createEnvelope` method signature is:

```
    public EnvelopeSummary createEnvelope(String accountId, EnvelopeDefinition envelopeDefinition, EnvelopesApi.CreateEnvelopeOptions options)
```

The `EnvelopesApi.CreateEnvelopeOptions` class is used to set the API method’s query parameters. The class is defined as:

```
     public class CreateEnvelopeOptions
      {
      private String cdseMode = null;
      private String changeRoutingOrder = null;
      private String completedDocumentsOnly = null;
      private String mergeRolesOnDraft = null;
      private String tabLabelExactMatches = null;

      public void setCdseMode(String cdseMode){
      this.cdseMode = cdseMode;
      }
      public String getCdseMode() { return this.cdseMode;}

      public void setChangeRoutingOrder(String changeRoutingOrder) {
      this.changeRoutingOrder = changeRoutingOrder;
      }
      public String getChangeRoutingOrder() {
      return this.changeRoutingOrder;
      }

      public void setCompletedDocumentsOnly(String completedDocumentsOnly)    {
    this.completedDocumentsOnly = completedDocumentsOnly;
      }
      public String getCompletedDocumentsOnly() {
        return this.completedDocumentsOnly;
      }

      public void setMergeRolesOnDraft(String mergeRolesOnDraft) {
        this.mergeRolesOnDraft = mergeRolesOnDraft;
      }
      public String getMergeRolesOnDraft() {
      return this.mergeRolesOnDraft;
      }

    public void setTabLabelExactMatches(String tabLabelExactMatches) {
        this.tabLabelExactMatches = tabLabelExactMatches;
      }
      public String getTabLabelExactMatches() {
        return this.tabLabelExactMatches;
      }
      }
```

The class fields in camelCase correspond to the API endpoint’s query parameters.

### [com.docusign.esign.client](https://github.com/docusign/docusign-esign-java-client/tree/master/src/main/java/com/docusign/esign/client) namespace

This namespace contains the classes needed to manage the overall API experience. These include the classes needed to instantiate a client element to make API calls and the classes used for authentication and exception handling. You will need to include this namespace to be able to use the Docusign eSignature API correctly.

### Using the SDK

To make eSignature REST API calls with the SDK, you need:

- A valid OAuth access token.
- The base path for the API call.
- For most API calls, you’ll also need the relevant `accountId`. Note that it is common for a user to be a member of multiple accounts.

### Multithreaded Environments

The Java SDK supports use in multithreaded environments. Docusign recommends creating an instance of the `ApiClient` object per thread in multithreaded environments to avoid potential issues such as race conditions (as in racing to overwrite one another) or the requirement of a shared caching system, where you need to be concerned with validating states for data integrity, spending extra computation cycles in the process. Creating an `ApiClient` instance per thread also helps ensure the Isolation principle in the [ACID](https://en.wikipedia.org/wiki/ACID) methodology.

The following code demonstrates how to use the Java SDK in a multithreaded environment. The `DSThread` class extends the built-in `Thread` method. It provides a signer name and email address for the envelopes being sent via API. The DS API Envelope object, named `DSEnvelope`, contains a `createEnvelope` class that has all of the Docusign API logic used to generate an OAuth token and send an envelope. To make everything work, an app.java file calls the `DSThread` class and can create any number of envelopes specified. This `DSThread` class then creates a copy of the DS API object for each envelope being sent:

App.java

```
package multi_thread;

public class app {
    public static void main (String[] args) throws InterruptedException {

        for (int i = 1; i <= 15; i++) {
            String threadName = Integer.toString(i);
            DSThread n = new DSThread(threadName + ": ");
            n.start();
        }

        System.out.println("Main thread");

    }
}
```

DSThread.java

```
package multi_thread;

import com.docusign.esign.client.ApiException;
import java.io.IOException;

public class DSThread extends Thread {

    public DSThread(String name) throws InterruptedException {
        super(name);
    }

    @Override
    public void run() {

        System.out.print(this.getName());
        System.out.println( "Sending a DS Envelope via a thread");

        DSEnvelope envelope = new DSEnvelope();
        try {
            String output = envelope.createEnvelope("Sammuel.Signer@dxtr.com", "Samuel Signer");
            System.out.println("EnvelopeID: " + output);
        } catch (ApiException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

DSEnvelope.java

```
package multi_thread;

import com.docusign.esign.api.EnvelopesApi;
import com.docusign.esign.client.ApiClient;
import com.docusign.esign.client.auth.OAuth;
import com.docusign.esign.client.auth.OAuth.OAuthToken;
import com.docusign.esign.client.auth.OAuth.UserInfo;
import com.docusign.esign.client.auth.OAuth.Account;
import com.docusign.esign.client.ApiException;
import com.docusign.esign.model.*;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.Arrays;

public class DSEnvelope {

    public String createEnvelope(String signerEmail, String signerName) throws IOException, ApiException {

        Timestamp timestamp = new Timestamp(System.currentTimeMillis());
        // Setup OAuth token
        // Get access token and accountId
        ApiClient apiClient = new ApiClient("https://demo.docusign.net/restapi");
        apiClient.setOAuthBasePath("account-d.docusign.com");
        ArrayList<String> scopes = new ArrayList<String>();
        scopes.add("signature");
        scopes.add("impersonation");
        byte[] privateKeyBytes = Files.readAllBytes(Paths.get("path\to\your\private.key"));
        OAuthToken oAuthToken = apiClient.requestJWTUserToken(
            "integrationKey",
            "impersonatedUserGuid",
            scopes,
            privateKeyBytes,
            3600);
        String accessToken = oAuthToken.getAccessToken();
        UserInfo userInfo = apiClient.getUserInfo(accessToken);
        String accountId = userInfo.getAccounts().get(0).getAccountId();
        apiClient.addDefaultHeader("Authorization", "Bearer "+ accessToken);

        EnvelopesApi envelopesApi = new EnvelopesApi(apiClient);

            // Create envelopeDefinition object
            EnvelopeDefinition envelope = new EnvelopeDefinition();
            envelope.setEmailSubject("Please sign this document set");

            // Create tabs object
            SignHere signHere = new SignHere();
            signHere.setDocumentId("1");
            signHere.setPageNumber("1");
            signHere.setXPosition("191");
            signHere.setYPosition("148");
            Tabs tabs = new Tabs();
            tabs.setSignHereTabs(Arrays.asList(signHere));
            // Set recipients
            Signer signer = new Signer();
            signer.setEmail(signerEmail);
            signer.setName(signerName + " executed: " + timestamp.toString());
            signer.recipientId("1");
            signer.setTabs(tabs);

            Recipients recipients = new Recipients();
            recipients.setSigners(Arrays.asList(signer));
            envelope.setRecipients(recipients);

            // Add document
            Document document = new Document();
            document.setDocumentBase64("VGhhbmtzIGZvciByZXZpZXdpbmcgdGhpcyEKCldlJ2xsIG1vdmUgZm9yd2FyZCBhcyBzb29uIGFzIHdlIGhlYXIgYmFjay4=");
            document.setName("doc1.txt");
            document.setFileExtension("txt");
            document.setDocumentId("1");
            envelope.setDocuments(Arrays.asList(document));

            envelope.setStatus("sent");

            EnvelopeSummary results = envelopesApi.createEnvelope(accountId, envelope);
            return results.getEnvelopeId();

}

}
```

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
