---
title: Docusign Monitor eSignature Alerts
source_url: https://support.docusign.com/s/document-item?language=en_US&bundleId=gso1581445176035&topicId=refd45c3b91-27da-49ee-aba6-f946c7e203da.html&_LANG=enus
site: support.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T21:18:17Z'
---

# Docusign Monitor eSignature Alerts

Review descriptions and recommended actions for Docusign Monitor eSignature, Admin settings, and login and security alerts.

Here are Docusign Monitor eSignature, Admin settings, Login and security alert descriptions and recommended actions.

Note: If the alert actions were unauthorized, you can:

- [Remove Users from Accounts](https://support.docusign.com/s/document-item?bundleId=pik1583277475390&topicId=uwb1583277426266.html&_LANG=enus).
- Change or revoke the user's administrative privileges as described in the [Delegated Permissions](https://support.docusign.com/s/document-item?bundleId=pik1583277475390&topicId=gih1583277347533.html&_LANG=enus) article.

## eSignature alerts

Administrators can use Monitor to track these eSignature activity alerts.

| Alert | Generated when: | Recommendations |
| --- | --- | --- |
| Autoplace scope changed | User changed [Autoplace](https://support.docusign.com/s/document-item?bundleId=gbo1643332197980&topicId=ytr1578456405118.html&_LANG=enus) settings. | Verify that settings changes were intentional. |
| Bulk envelope sent | User successfully initiates an envelope bulk send at least `n` times. The `n` is a configurable threshold. The default is one. | Investigate user activity and contact the user if this behavior is unusual. |
| Possible signer impersonation | Matching IP, device type, application, and browser fingerprint suggest the sender signed the envelope with the signer's account. | Investigate whether the sender had a valid reason to use the same device as the signer. |
| Recipient authentication disabled | Updated account security policy. Note: This alert is available for the Monitor Free Edition. | Verify that settings changes were intentional. |
| Unusual document download volume | User downloads more than `n` envelopes in an hour.  The `n` is a configurable threshold. The default is 15. | Investigate user activity and contact the user if this behavior is unusual. |
| Unusual envelope deletion volume | User deletes more than `n` envelopes in an hour.  The `n` is a configurable threshold. The default is 20.  Note: This alert is available for the Monitor Free Edition. | Investigate user activity and contact the user if this behavior is unusual. Note: This alert's alert threshold currently includes draft envelopes. Starting in July, it will only consider sent and completed envelopes. |

## Admin settings alerts

Administrators can use Monitor to track these Monitor Administration settings activities.

| Alert | Generated when: | Recommendations |
| --- | --- | --- |
| Bulk account settings export | The user initiated a bulk accounts settings export. | Ensure that this settings data was only shared with the right users. |
| Bulk users export | User initiated a bulk export of user data, including name, email, and permission profile. | Ensure that this sensitive data was only shared to the right users. |
| Delegated administrators assigned | Assigned `n` or more Account delegated administrators in one hour. The `n` is a configurable threshold. The default is five. | Verify that permission changes were intentional. |
| Document retention policy changed | Changed the account's document retention. | Verify that settings changes were intentional. |
| Legal disclosure setting changed | Changed the account's legal disclosure setting | Verify that settings changes were intentional. |
| Watermark configuration changed | Changed the account's watermark configuration | Verify that settings changes were intentional. Review your account's watermark settings as described in the [Set Watermarks](https://support.docusign.com/s/document-item?bundleId=pik1583277475390&topicId=zoa1644444718595.html&_LANG=enus) article. |

## Login and security alerts

Administrators can use Monitor to track these login and security activities.

| Alert | Generated when: | Recommendations |
| --- | --- | --- |
| Multiple login failures | A user had `n` or more login failures in the past hour. The `n` is a configurable threshold. The default is six. Multiple failed logins within **1 minute** count as one failure.  Note: [Claim at least one domain](https://support.docusign.com/s/document-item?bundleId=rrf1583359212854&topicId=gso1583359141256.html&_LANG=enus). | Reset the user's password and enforce SSO to improve security. |
| Non-domain member activity | Actions involving a non-domain user activity were detected This alert is only generates if the action was taken by the non-domain user, regardless of the event recipient.  Note: [Claim at least one domain](https://support.docusign.com/s/document-item?bundleId=rrf1583359212854&topicId=gso1583359141256.html&_LANG=enus). | Claim this domain to centralize control and manage the user's access. |
| Password changed from new location | The user changed their password from a location more than `m`  km from any location that they have logged in from in the previous 21 days. The `n` is a configurable threshold.  The default is 200 km.  Note: This alert is available for the Monitor Free Edition. | Reset the user's password if this was unauthorized and enforce SSO to improve security. |
| Password rules changed | The account's [password rules](https://support.docusign.com/s/document-item?bundleId=pik1583277475390&topicId=yfn1583277328637.html&_LANG=enus) were modified within one hour. | Verify that settings changes were intentional and enforce SSO to improve security. |
| Simultaneous login | The user logged on from a location more than `n` km from any location to which they’ve logged on over the last hour. The `n` is a configurable threshold. The default is 200 km.  Note: [Claim at least one domain](https://support.docusign.com/s/document-item?bundleId=rrf1583359212854&topicId=gso1583359141256.html&_LANG=enus). | Check if this IP address and location is known and contact the user if this behavior is unusual. This alert now incorporates browser fingerprint data. It only generates when sessions occur from different devices. |
| SSO bypass enabled for user | A user was permitted to use Username/Password logon instead of SSO. Note: [Claim at least one domain](https://support.docusign.com/s/document-item?bundleId=rrf1583359212854&topicId=gso1583359141256.html&_LANG=enus). | Verify that settings changes were intentional and enforce SSO to improve security. |
| SSO login policy changed | Changed SSO login policy of a claimed domain. Note: [Claim at least one domain](https://support.docusign.com/s/document-item?bundleId=rrf1583359212854&topicId=gso1583359141256.html&_LANG=enus). | Verify that settings changes were intentional and enforce SSO to improve security. |
| New proxy usage | A user used a new proxy to mask their IP address and location. | Check whether this IP address and location are known and contact the user if this behavior is unusual. |
| Unauthorized IP address activity | Activity was detected from locations not included in the  [IP Safe List](https://support.docusign.com/s/document-item?bundleId=gso1581445176035&topicId=mfq1645630427780.html&_LANG=enus "Learn how to create a list of trusted IP addresses with the Docusign Monitor IP Safe List feature."). | Investigate user activity and update the IP Safe List as needed. |

## Threats and abuse

Administrators can use Monitor to track these account threat activities

| Alert | Generated when: | Recommendations |
| --- | --- | --- |
| Abuse Report Received | This alert generates when a recipient selects Report abuse in a Docusign email to flag content sent from your organization. | As an Admin, investigate the abuse reason, and check whether users opened the email. |
