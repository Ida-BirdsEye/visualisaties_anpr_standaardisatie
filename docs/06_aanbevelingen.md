# 6. Aanbevelingen

Op basis van de uitgewerkte visualisaties en de bijbehorende datamodellen volgen hieronder de belangrijkste aanbevelingen voor de verdere ontwikkeling van de ANPR-datastandaard en de implementatie binnen het project.

## 1. Standaardiseren van veldnamen en waarden
Om datalevering tussen gemeenten, leveranciers, CBS en digital twin-partijen te uniformeren, moeten veldnamen en enumeraties consistent worden vastgelegd:

- **Consistentie in naamgeving:** Digital twin-leveranciers werken bij voorkeur met *camelCase*, terwijl cameraleveranciers *snake_case* aanleveren. Stem dit waar mogelijk op elkaar af.  
- **Consistentie in taalgebruik:** CBS hanteert Nederlandse veldnamen, terwijl aangeleverde data vaak Engelstalig is. Zorg waar mogelijk voor één uniforme taalkeuze.  
- Duidelijke enumeraties voor richtingwaarden (Inbound / Outbound, Obverse / Reverse).  
- Gebruik van ISO-standaarden voor datum- en tijdvelden.  
- Eenduidige benaming en groepering van voertuigkenmerken zoals carrosserietypen. Dit voorkomt parsingproblemen, fouten en interpretatieverschillen bij dashboards en API’s.  
- Zorg voor een gestandaardiseerde `zoneId` met een numerieke code, bij voorkeur bij de bronhouder (NDW).  

## 3. Borgen van aansluiting op CBS-statistische beveiliging
De visualisaties tonen dat vooral kruisverbandtabellen snel leiden tot kleine aantallen. Daarom is het noodzakelijk dat:

- Waarden onder de drempel voor statistische beveiliging niet worden teruggegeven en als lege velden verschijnen.  
- Tabellen worden opgesplitst wanneer meerdere kenmerken tegelijk tot kleine cellen leiden.  

Het CBS heeft aangegeven de voorgestelde tabelstructuur nog te beoordelen op formele handhaafbaarheid van statistische beveiliging.

## 4. Richting een API-gebaseerde datastructuur
Voor duurzame inzet, herhaalbaarheid en schaalbaarheid moet worden toegewerkt naar:

- één uniforme API-definitie voor ANPR-data-aanlevering;  
- één uniforme API-output voor gemeenten en digital twin-partijen;  
- een versieerbaar datamodel met duidelijke governance.  

## 5. Verbeterde governance en datakwaliteitsproces
Om datakwaliteit te borgen is het aan te bevelen dat:

- Gemeenten verantwoordelijk blijven voor het correct configureren van zonegrenzen.  
- Leveranciers zorgen voor consistente en tijdige metadata.  

## 6. Heldere afstemming met gemeenten rondom registratie ZE-zonering, cameralocaties en venstertijden
Goede afstemming voorkomt fouten in in-/uitrijdberekeningen, ondersteunt consistente datasets en verbetert de betrouwbaarheid van beleidsinzichten.

- Zorg voor duidelijke communicatie met gemeenten over het correct aanleveren en actueel houden van ZE-zonepolygonen en venstertijden in NDW of NPR.  
- Gemeenten moeten actief controleren welke camera’s door leveranciers aan het CBS worden doorgegeven.  
- Controleer of deze camera’s technisch en geografisch juist gekoppeld kunnen worden aan de ZE-zonepolygonen.  
