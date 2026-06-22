---
title: Salesforce Connected App Security Changes
source_url: https://support.docusign.com/s/document-item?language=en_US&bundleId=izj1586134369853&topicId=refbdaee1ac-b187-4df9-94f2-a094f9f47ef2.html&_LANG=enus
site: support.docusign.com
breadcrumb: []
scraped_at: '2026-06-22T20:01:51Z'
---

# Salesforce Connected App Security Changes

Learn about the actions that you must take to use Docusign apps after
Salesforce security changes.

Important: You are not required to make any changes if
you have taken the following steps:

- Installed the Docusign connected app.
- Set the OAuth policy to Admin-approved users are pre-authorized.

  Note: Changing policy revokes existing
  user tokens. Existing users must re-authorize.

## What is changing with Salesforce connected app security?

Starting in September 2025, Salesforce began enforcing [restrictions for uninstalled connected apps](https://help.salesforce.com/s/articleView?id=005132365&type=1). This usage
restriction blocks access to uninstalled connected apps. If you have not installed
the Docusign connected app and assigned permissions, your users
cannot access Docusign apps.

As part of this change, Salesforce created the Approve uninstalled connected apps user permission (defaulted to System
Administrator standard profile.)

## How do these security changes impact Docusign integrations?

Connected apps installed before the security change continue to function
without interruption. Take action only if you did not install the connected app
before the changes.

## What is an uninstalled connected app?

An [uninstalled connected app](https://help.salesforce.com/s/articleView?id=xcloud.connected_app_how_to_install.htm&type=5) is an application in your
organization that has not been installed by a System Administrator. Organizations
integrated with Docusign contain an uninstalled connected app
named DocuSign on the Connected Apps OAuth
Usage page. By default, this application is not installed, and must
be manually installed by a System Administrator. ![A screenshot displays the install button highlighted on the Docusign connected app OAuth Usage page.](https://docusign-be-prod.zoominsoftware.io/api/bundle/izj1586134369853/page/images/A_screenshot_displays_the_install_button_highlighted_on_the_Docusign_connected_app_OAuth_Usage_page.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6ImRvY3VzaWduX3Byb2R1Y3Rpb24iLCJleHAiOjE3ODIxNTYyNzksInNoZWFmIjoiaXpqMTU4NjEzNDM2OTg1MyJ9.vsJ-kzlvkfxXKfiEJz3Ty6qI0QGcBsnembXUcednlzw&_LANG=enus "A screenshot displays the install button highlighted on the Docusign connected app OAuth Usage page.")

## Which Docusign managed packages contain the connected app?

The following Docusign for Salesforce packages contain the Docusign connected app:

- Docusign Apps Launcher (Namespace: dfsle)
- Docusign for Salesforce (Legacy Namespace: dsfs)
- FileIt (Legacy Namespace: SpringCMEos)

## How are new users impacted?

If you have not installed the app before the security change, your new
users cannot access the Docusign connected app. Users see the
authorization button, but a Salesforce OAuth error displays after they enter their
Docusign credentials: We can't authorize you because
of an OAuth error. For more information, contact your Salesforce
administrator.

## How are existing users impacted?

If you never installed the app, existing users can access it if they meet the
following criteria:

- The user has previously authorized the app.
- The app isn’t using the [OAuth 2.0 device flow](https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_device_flow.htm&language=en_US&type=5).

## Does Docusign Apps Launcher use OAuth 2.0 device flow?

No. Docusign Apps Launcher does not use OAuth 2.0 device flow.

## What actions should I take?

[Install the connected app to grant Docusign
for Salesforce access to new users](https://support.docusign.com/s/articles/Install-the-DocuSign-Apps-Launcher-to-Manage-Connected-Apps-in-Salesforce-Setup).

Note: Salesforce
and Docusign recommend selecting Admin-approved
users are pre-authorized. Each user must enter credentials to
gain Docusign for Salesforce app access if you select
All users may self-authorize.

## What happens when I change the connected app policy?

Make the following changes when you update the Permitted Users
setting to Admin approved users are pre-authorized:

Administrators
:   - All Apps Launcher apps: Add all necessary
      profiles and permission sets to the Docusign
      connected app. An error message displays for users not included
      in these profiles and permission sets: User is not
      admin approved to access this app.
    - CLM for Salesforce: [Disconnect your account and
      preserve user settings](https://support.docusign.com/s/document-item?bundleId=izj1586134369853&topicId=oks1610512362945.html&_LANG=enus "Learn how to disconnect Docusign from Salesforce while preserving user settings with the Docusign TroubleShooting tool.") if you use CLM Document
      Generation. Otherwise, a Salesforce session is
      invalid error displays when users try to generate
      agreements.

Existing users
:   Authorized users must re-authorize. Steps to re-authorize vary for each
    installed package:

    - Docusign Apps Launcher: [Activate your Docusign
      for Salesforce user](https://support.docusign.com/s/document-item?bundleId=qob1643667997351&topicId=ymi1586134213877.html).
    - Docusign Connect for Salesforce (Legacy):
      [Reconfigure your login with Docusign Connect](https://support.docusign.com/s/document-item?bundleId=gab1637077302276&topicId=tsk6312c996-938f-4f24-b11f-9da2f7887493.html). There is no
      option to authorize within the legacy Docusign
      for Salesforce integration.
    - FileIt (Legacy SpringCM): Take no action.
      Existing users are already authorized to use SpringCM FileIt. If
      users must re-authorize, use these procedures:
      - [Configure FileIt app security
        settings](https://support.docusign.com/s/document-item?bundleId=dsa1643667928464&topicId=qgu1583188662524.html).
      - [Connect Salesforce to
        SpringCM](https://support.docusign.com/s/document-item?bundleId=dsa1643667928464&topicId=btt1576610138405.html).

## How do I resolve connected app errors?

User is not admin approved to access this app
:   Resolution: Install and configure the Docusign
    connected app. Add the missing profile or permission set if you have
    already installed the app.

You have not granted or have revoked your consent to be impersonated by Docusign Apps Launcher
:   Resolution: Install the Docusign connected app. [Refresh the user's consent flow](https://support.docusign.com/s/articles/DAL-Error-You-have-not-granted-or-have-revoked-your-consent-to-be-impersonated-by-DocuSign-Apps-Launcher) if you have
    already installed the app.

We can't authorize you because of an OAuth error. For more information, contact your Salesforce administrator
:   Resolution 1: Install the Docusign connected app. Add access to missing profiles
    or permission sets on the Connected App Detail page
    if you have already installed the app.
:   Resolution 2: Install the Docusign connected app. Go to Setup >  Connected Apps OAuth Usage and choose All users may
    self-authorize for the Docusign
    connected app.

Salesforce session is invalid
:   Resolution 1: Install the Docusign connected app. [Disconnect and reconnect your account and
    preserve user settings](https://support.docusign.com/s/document-item?bundleId=izj1586134369853&topicId=oks1610512362945.html&_LANG=enus "Learn how to disconnect Docusign from Salesforce while preserving user settings with the Docusign TroubleShooting tool.") after changing OAuth policy to
    All users may self-authorize.
:   Resolution 2: Enable Allow
    Visualforce pages to access APIs if either
    Restrict Access to APIs with Connected
    Apps or Restrict Customers and Partners
    from Access APIs is enabled.
