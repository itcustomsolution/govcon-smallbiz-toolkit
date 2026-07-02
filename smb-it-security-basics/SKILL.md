---
name: smb-it-security-basics
description: The pragmatic security baseline a competent managed service provider implements on day one for a small office. Covers multi-factor authentication, patching cadence, the 3-2-1 backup rule with restore testing, email security, least-privilege access reviews, and clean offboarding. Use as a starting checklist for a small business (roughly 5 to 50 people) that wants to close the most common and most exploited gaps without buying a security program it cannot run. Ordered by impact, so a small team can work top to bottom.
---

# Small-Office IT Security Baseline

Most breaches at small organizations do not come from exotic attacks. They come from a reused password with no second factor, an unpatched machine, a mailbox with no phishing protection, an over-privileged account nobody reviews, or a departed employee whose access was never revoked. This baseline closes those gaps in the order that matters most. It is what a competent provider sets up in the first engagement, and none of it requires a large budget.

Work top to bottom. The earlier items block the most common attacks.

---

## 1. Multi-factor authentication (MFA), everywhere it counts

Passwords get phished, guessed, and reused. A second factor stops the large majority of account-takeover attempts.

- [ ] **Turn on MFA for email and identity first.** Microsoft 365, Google Workspace, or whatever hosts your mail and single sign-on is the crown jewel. Compromise there cascades everywhere.
- [ ] **Then MFA every other business-critical account:** banking, payroll, accounting, your domain registrar and DNS, cloud consoles, remote-access tools, and any admin portal.
- [ ] **Prefer app-based authenticators or hardware security keys over SMS.** SMS codes can be intercepted or SIM-swapped. Use them only when nothing better is available.
- [ ] **Protect administrator accounts hardest.** Require phishing-resistant MFA (security keys or passkeys) on admin accounts if the platform supports it.
- [ ] **Pair MFA with a password manager** so every account gets a long, unique password and nobody reuses one across services.

## 2. Patch on a cadence you actually keep

Attackers weaponize known vulnerabilities fast. Patching is the unglamorous control that closes those doors.

- [ ] **Enable automatic updates for operating systems** on every workstation and server where it is safe to do so.
- [ ] **Patch browsers and their extensions,** which are a common entry point.
- [ ] **Patch third-party applications,** not just the OS. Productivity suites, PDF readers, remote-access tools, and line-of-business apps all need updates.
- [ ] **Set a written cadence.** Critical/actively-exploited patches within days; routine patches monthly. Track which machines are behind.
- [ ] **Retire end-of-life software and hardware.** Anything the vendor no longer patches is a permanent hole. Plan replacement before support ends.
- [ ] **Keep firmware current** on firewalls, routers, and network gear, which are frequently targeted and frequently forgotten.

## 3. Backups: the 3-2-1 rule, and prove they restore

Backups are your last line against ransomware, hardware failure, and mistakes. A backup you have never restored is a hope, not a backup.

- [ ] **Follow 3-2-1:** at least **3** copies of your data, on **2** different types of media/storage, with **1** copy kept **off-site** (or in a separate cloud account/region).
- [ ] **Keep at least one copy offline or immutable.** Ransomware deliberately hunts and encrypts reachable backups. An offline copy, or an immutable/write-once cloud backup, survives that.
- [ ] **Back up what actually matters:** email, file storage, business-critical SaaS data (many SaaS platforms do NOT back up your data for you in a way you can restore), servers, and endpoints holding local data.
- [ ] **Test restores on a schedule.** Actually restore a sample of files, and periodically a whole system, and time it. You are testing both that the backup works and that you can meet your recovery-time needs.
- [ ] **Write down your recovery objectives:** how much data you can afford to lose (recovery point) and how fast you must be back (recovery time). Size the backup approach to those.

## 4. Email security and phishing defense

Email is the number-one delivery mechanism for attacks on small businesses.

- [ ] **Turn on the anti-phishing and anti-malware protections** your mail platform includes, and tune them rather than leaving defaults.
- [ ] **Publish SPF, DKIM, and DMARC records** for your domain so others cannot easily spoof your email and so your legitimate mail is trusted. Move DMARC toward an enforcing policy once you have confirmed your legitimate senders pass.
- [ ] **Warn on external mail.** Tag messages from outside the organization so staff know when a "CEO" request actually came from a stranger.
- [ ] **Train people briefly and regularly** to recognize phishing, especially payment-change and gift-card requests (business email compromise). Give them a fast, no-blame way to report suspicious mail.
- [ ] **Verify money and banking changes out of band.** Any request to change payment details or wire funds gets confirmed by a phone call to a known number, never by replying to the email.

## 5. Least-privilege access and regular reviews

Accounts accumulate access over time. Excess access turns one compromised account into a company-wide incident.

- [ ] **Give people the minimum access they need to do their job,** and no standing administrator rights on their day-to-day accounts.
- [ ] **Separate admin accounts from daily-use accounts.** Admins should use a normal account for email and browsing and a distinct privileged account only when performing admin tasks.
- [ ] **Review access on a schedule** (quarterly is reasonable for a small firm). Who can reach what? Remove access that is no longer needed. Pay special attention to shared drives, finance systems, and cloud consoles.
- [ ] **Inventory your accounts and your data.** You cannot protect what you do not know exists. Keep a simple list of systems, who has access, and where sensitive data lives.
- [ ] **Control third-party and vendor access.** Contractors and vendors get scoped, time-limited access, tracked and removed when the engagement ends.

## 6. Clean, prompt offboarding

A departed employee with live credentials is a standing risk and a common breach cause.

- [ ] **Have a written offboarding checklist** and run it the same day someone leaves.
- [ ] **Disable accounts immediately,** starting with email and single sign-on, then every other system.
- [ ] **Revoke MFA devices, app passwords, API keys, and any shared credentials** the person knew. Rotate shared secrets they had access to.
- [ ] **Reclaim company devices** and confirm data on them is handled per policy.
- [ ] **Reassign or preserve their data and mailbox** before deletion so you do not lose business records.
- [ ] **Remove them from vendor portals, cloud consoles, and building/remote access** too, not just internal systems.

---

## A few more that pay off quickly

- [ ] **Endpoint protection** (modern antivirus / endpoint detection) on every workstation and server, kept updated.
- [ ] **Full-disk encryption** on laptops and phones so a lost device is not a data breach.
- [ ] **A firewall and a segmented network** at minimum separate guest Wi-Fi from business systems.
- [ ] **A short, written incident-response plan:** who to call, how to isolate a machine, where the backups are, and how to reach your provider and any legal or notification contacts. A one-page plan practiced once beats a perfect plan nobody has read.
- [ ] **Secure remote access.** No exposed remote-desktop directly on the internet; use a VPN or a managed access tool, always behind MFA.

---

*Part of the GovCon Small-Biz Toolkit. Provided free under the MIT License. This is a general baseline, not a compliance program or a substitute for a risk assessment tailored to your organization. Where you have regulatory obligations, map these controls to the specific framework that applies to you.*
