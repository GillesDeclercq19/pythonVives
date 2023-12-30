Doel:
Simpele gebruiker en product creatie, waarbij de opslagen gegevens kunnen verwerkt worden in een rapport.

Functionaliteiten:
Deze applicatie kan een user aanmaken via een naam en e-mail. Deze user kan aangepast worden. Er kan ook een product toegevoegd worden via een naam en prijs. Er is een mogelijkheid om alle users of producten die opgeslagen zijn in de database in een rapport te verwerken, dit rapport kan zowel een csv als excel bestand zijn.


Instructies:
Voor de database: Maak bijvoorbeeld een mapje aan op de C-schijf genaamd "project_db". bv: C:\project_db (dit voorbeeld path zit al in de settings.ini file). Je kan deze locatie ook veranderen maar dan moet je de path aanpassen in de settings.ini! Mocht er geen database file staan in de directory dan zal de applicatie een db file zelf creëren.
Open een cmd en ga naar de map waar de "app" map zich bevindt.
Voer commando "python -m venv venv" uit.
Voer commando "venv\Scripts\activate" uit.
Voer commando "pip install -r requirements.txt" uit.
Voer app uit via commando "python app/main.py".

