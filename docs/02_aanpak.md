# 2. Aanpak

Binnen de werkgroep is onderzocht welke inzichten gemeenten nodig hebben, welke datavelden en onderliggende tabellen noodzakelijk zijn en hoe deze gegevens het beste kunnen worden weergegeven. Visualisaties fungeerden hierbij als middel om databehoeften concreet te maken en te toetsen of het voorgestelde datamodel voldoende is om de gewenste inzichten te leveren. Daarbij is ook meegenomen in hoeverre de beoogde visualisaties passen binnen de statistische beveiligingstoets van het CBS, zodat de inzichten die uiteindelijk aan gemeenten worden geleverd voldoen aan de eisen voor anonimiteit en statistische betrouwbaarheid.

## 2.1 Uitgevoerde activiteiten

Voor de totstandkoming van de visualisatieconcepten zijn de volgende activiteiten uitgevoerd:

- Deelname aan drie-wekelijkse werkgroepbijeenkomsten en tussentijdse stand-ups.
- Inventarisatie van de inzichten die gemeenten met ANPR-data willen ontsluiten, onder andere rond ZE-zones, emissie-eisen en logistieke stromen.
- Uitwerken van visualisatievoorbeelden (wireframes) in Figma, gericht op structuur en informatiehiërarchie in plaats van definitieve vormgeving.
- Uitwerken van onderliggende tabellen en datavelden per visualisatie, inclusief naming conventions, aggregatieniveaus en koppelingen met CBS-verrijking.
- Toetsing van de voorstellen met betrokken partijen (gemeenten, leveranciers, CBS, DMI, digital twin-leveranciers).
- Online discussie en iteratie via GitHub Issues, zodat opmerkingen en voorstellen traceerbaar en herbruikbaar zijn binnen het project.

## 2.2 Positie in de ANPR-keten

Het volledige ANPR-proces kent meerdere schakels, van detectie tot beleidsvisualisatie:

1. ANPR-camera’s registreren kentekens op strategische locaties in en rond de stad.
2. ANPR-leveranciers verwerken deze ruwe detecties en leveren data in een afgesproken formaat door aan het CBS.
3. Het CBS verrijkt de gegevens met onder andere voertuigkenmerken (zoals emissieklasse, brandstoftype en voertuigtype), herkomstinformatie en sectorinformatie (SBI), en past statistische beveiliging toe.
4. De output van het CBS bestaat uit geaggregeerde, beveiligde tabellen, die periodiek beschikbaar worden gesteld aan partijen zoals Esri en Argaleo.
5. Digital twin-leveranciers laden deze tabellen in hun platformen (bijvoorbeeld ArcGIS en Digitwin), waar de data wordt gecombineerd met andere geografische en beleidsinformatie.
6. Gemeenten raadplegen de resulterende dashboards en digital twins voor beleidsvorming en monitoring van stadslogistiek en ZE-zones.

Dit rapport richt zich uitsluitend op de **laatste deelstap in deze keten**: de overgang van verrijkte en geaggregeerde CBS-tabellen naar gestandaardiseerde visualisaties in digital twin-omgevingen. Daarbij ligt de nadruk op:

- welke tabellen en velden minimaal nodig zijn voor beleidsrelevante visualisaties;
- hoe deze velden het beste gestructureerd en benoemd kunnen worden;
- hoe visualisaties rekening houden met de CBS-regels voor statistische beveiliging;
- hoe dit alles inpasbaar is in de bestaande dashboards en digital twins van gemeenten.

De resultaten in dit document zijn daarmee zowel een ontwerpreferentie voor dashboards als een inhoudelijke onderbouwing voor de verdere uitwerking van het ANPR-datamodel en bijbehorende API’s.
