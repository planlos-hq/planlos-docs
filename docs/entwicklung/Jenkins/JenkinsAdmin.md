# Administration
## Einrichtung
Zunächst muss ein Jenkins Server eingerichtet werden.
Es wird angenommen, dass ein vorgeschalteter HTTP-Server existiert, der Anfragen mittels Reverse-Proxy weiterleitet.

Dann wird ein Admin-Account angelegt.

Um Jenkins Zugriff auf die relevanten Repos zu gestatten muss eine GitHub App eingerichtet werden. (es kann bei Nachfrage auch die bestehende auf einen neuen Besitzer übertragen werden)

- GitHub.com öffnen
- Profilbild oben rechts wählen
- Settings wählen
- Developer settings wählen
- auf vorausgewähltem GitHub Apps Tab bleiben oder zu diesem wechseln
- New GitHub App wählen
- Sinnvollen GitHub App name wählen (z.B. Jenkins-Stundenplan; Achtung: Dieser muss global eindeutig sein)
- Homepage URL (beliebig z.B. URL der Jenkins-Instanz)
- Callback URL (beliebig, da keine Verwendung)
- Webhook Active abgeschaltet lassen (betreffen Events bezüglich der Anwendung selbst)
- Permissions hinzufügen (ausschließlich Repository permissions notwendig):
    - Checks (Read and write)
    - Contents (Read-only)
    - Webhooks (Read and write)
- Scope der Anwendung (Where can this GitHub App be installed) auf "Any account" stellen, um in der Organisation installieren zu können
- Create GitHub App wählen

Es muss außerdem ein Client secret und ein private key generiert werden um Jenkins zu erlauben im Namen dieser Anwendung zu handeln. Diese (sowie die App ID) muss Jenkins hinzugefügt werden:

- Jenkins Einstellungen öffnen
- Credentials wählen
- System wählen
- Global credentials (unrestriced) wählen
- Add Credentials wählen
- GitHub App als Kind auswählen
- ID wählen (z.B. github-app)
- App ID mit App ID aus GitHub Seite füllen
- Private Key einfügen
    - Konvertieren mittels `openssl pkcs8 -topk8 -inform PEM -outform PEM -in foobar.private-key.pem -out new-key.pem -nocrypt`
    - korrektes Format:
```
-----BEGIN PRIVATE KEY-----
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXX
-----END PRIVATE KEY-----
```

Nun kann die App den relevanten Repositories hinzugefügt (installiert) werden:

- Zu der App auf GitHub navigieren (siehe oben)
- Install App Tab wählen
- Organisation wählen und Install oder Zahnrad wählen
- Repositories auswählen und bestätigen

Damit Jenkins Updates von GitHub erhalten kann muss der sog. WebHook-Mechanismus eingerichtet werden.
Hierfür muss ein Credential generiert (zum Beispiel mit einem Passwortgenerator) und sowohl in Jenkins als auch im GitHub Repository eingestellt werden.

Zunächst die Einrichtung unter Jenkins:

- Jenkins Einstellungen öffnen
- Credentials wählen
- System wählen
- Global credentials (unrestriced) wählen
- Add Credentials wählen
- Secret text als Kind wählen
- Secret eintragen
- ID wählen (z.B. github-webhook)
- Create wählen

Nun muss dieses Secret als WebHook-Secret eingestellt werden:

- Jenkins Einstellungen öffnen
- System wählen
- zu GitHub scrollen
- Advanced aufklappen
- Unter Shared secret das vorher erstellte GitHub WebHook Secret wählen
- Signature algorithm auf SHA-256 stellen

Nun kann WebHooks für einzelne Jobs eingerichtet werden.

Um einen Job automatisch durch pushes zu starten, muss der Haken bei GitHub project gesetzt und die URL gesetz werden (z.B. `https://github.com/<org>/<repo>/`)

Zusätzlich muss ein Haken unter Triggers bei "GitHub hook trigger for GITscm polling" gesetzt werden.

Außerdem müssen die App Credentials eingestellt werden, um Lesezugriff auf private Repos zu erlauben.

Hierfür muss unter Pipeline -> Definition "Pipeline script from SCM" eingestellt werden. Unter SCM Git wählen, die Repository URL eintragen (z.B. `https://github.com/<org>/<repo>`) und  schließlich die App Credentials gewählt werden.
Wenn der Hauptbranch nicht `master` sonder `main` heißt muss unter Branches to build `*/master` zu `*/main` abgeändert werden.

Außerdem muss eventuell der Script Path geändert werden, wenn die Jenkinsdatei nicht im Root-Verzeichnis liegt und `Jenkinsfile` heißt.

Der letzte Schritt besteht darin die Webhooks im Repository einzurichten.
Hierfür muss in den Einstellungen des Repo der Tab Webhooks gewählt werden und ein neuer Webhook hinzugefügt werden. Es muss die Payload URL eingetragen werden (z.B. `https://<jenkins-host>/jenkins/github-webhook/`). Der Content type bleibt auf application/x-www-form-urlencoded stehen und das Secret muss eingetragen werden.

Außerdem sollte SSL verification eingeschaltet werden.

Für trigger events reicht "Just the push event".

Der Webhook muss auf "Active" gesetzt werden und hinzugefügt werden.

Nach Abschluss dieser Schritte sollte Jenkins nun in der Lage sein Jobs automatisch bei push anzustoßen und die Ergebnisse rückzumelden.
