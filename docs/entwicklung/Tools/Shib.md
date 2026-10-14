# Shibboleth

Shibboleth2 ist ein Zusammmenspiel aus dem Identity Server der Hochschule und der jeweiligen Server. Ein Server benötigt entsprechende Zertifikate und kann bei Authorisation bestimmte Datenfelder abfragen. Diese muss zwischen dem anfragenden Server und dem Sibboleth Server übereinstimmend konfiguriert werden. 

## Login

Um Shibboleth zu verwenden muss in dem jeweiligen Verzeichnis eine .htaccess Datei angelegt werden, die eine Authentifizierung mittels Shib anfordert.

```
AuthType shibboleth
ShibRedirectToSSL 443
ShibRequireSession On
require valid-user
```

Dieser Eintrag erzwingt das Login via shib und erlaubt nur den Zugriff auf das Verzeichnis, wenn eine Anmeldung mit einem existierenden User möglich war.

## Antwort

Wenn der Login **nicht** erfolgreich ist, wird die Seite nicht geladen. Wenn der Login erfolgt ist wird die Seite aufgerufen und die Server Variable `REMOTE_USER` gesetzt. Diese dient lediglich dazu, das weiterführende System über den Namen des eingeloggten Users zu informieren, um diesen ggf. für eine Hello Message oder das interne Rechtesystem zu verwenden. Andere Daten werden, alleine schon aus Datenschutzgründen, nicht weiter gegeben. 

### Einbettung

Im einfachen Fall kann man auf der Webseite eine JS Funktion integrieren und die Seite als php anlegen um die Server Variable auszulesen. 

```html
<!--  index.php  //-->
<html>
  <head>
    <script>
      function login(user)
      {
        ...
      }
      login(<"?php echo $_SERVER["REMOTE_USER"] ?">)
    </script>
  </head>
</html>
```

REMOTE_USER wäre leer, wenn der Login nicht erfolgreich wäre, aber wesentlich wichtiger wäre, dass die Seite nicht aufgerufen werden kann ohne die erfolgreiche Anmeldung im Shib. 

## Abmeldung

Theoretisch erfolgt die Abmeldung via `https://<host>/Shibboleth.sso/Logout`
Es ist etwas unklar, warum die Abmeldung nicht gut funktioniert. Prinzipiell sollte das Logout erfolgreich sein und auch eine Neuanmeldung erforderlich sein, wenn der Browser nach Logout geschlossen wurde. Insbesondere auf mobilen Endgeräten ist teilweise der Logout aber nicht richtig erfolgt, so dass beim Wiederaufruf der Seite die angemeldeten Nutzenden noch angemeldet waren.

## Nutzernamen unter Go abrufen
`r.Header.Get("Remote_user")`

## API Nutzerauthorisierung

Das Backend enthält eine Middleware die Anfragen ablehnt, deren Shibboleth-Nutzernamen nicht in der `authorized_user`-Tabelle vermerkt sind.

Um Nutzer dieser Tabelle hinzuzufügen, kann folgendes SQL verwendet werden:

`insert into authorized_user(shib_user_name) values ('u12345');`

Um Nutzer wieder zu entfernen:

`delete from authorized_user where shib_user_name = 'u12345';`

## Authentifizierung deaktivieren

Um die Authentifizierung zu Testzwecken oder Ähnlichem zu deaktivieren, kann die `NO_AUTH` Umgebungsvariable des Go-Backends gesetzt werden.
