*Structura unui framework BDD
1.Folder features - Contine fisiere scrise intr-un limbaj mai natural(gherkin) care sa descrie scenariile de business
 given (contextul in care se desfasoara actiunea)
 when (actiunea pe care o facem)
 then (deznodamantul -verificarea pe care vrem sa o facem)
2.Folder steps = Step definition files- maparea tehnica a fisierelor de business -feature files
3.Folder pages = Pagini de mapare pentru elementele din browser(POM -page object model)
-Vom avea fisiere pentru fiecare pagina web a aplicatiei
-base_page file - este o clasa ce contine metode care pot fi folosite in mai multe clase, (adica care sunt utile pentru toate paginile)
4.Fisiere browser -contine instructiuni de instalare si deschidere browser
5.Fisiser environment -contine instantierea tuturor claselor de tip pages

*Metodologii de lucru
1.Waterfall:
- stricta
- orice modificare necesara dupa inceperea proiectului va trebui implementata intr-un proiect nou
- se planuieste tot la inceput, apoi se dezvolta, se testeaza si se da in productie
- feedback-ul se primeste tarziu, la final si de regula se dezvolta multa functionalitate

2.Agile:
- mai putin stricta, este flexibila si organizata
- orice modificare aparuta in timpul implementarii se poate modifica pe parcurs
- se lucreaza in sprint-uri (de regula cicluri de 2 saptamani)
- intr-un sprint se planifica, se dezvolta, testeaza si se da in productie
- feedback-ul pentru produs de la clienti, se primeste dupa fiecare sprint si se poate implementa in urmatoarele sprint-uri
- (Scrum si Kanban, Scrumban)

Functionalitatiile se pot grupa in felul urmator:
1.Epic ->componente majore(ex:pagina de cumparaturi)
2.Story ->functionalitati independente din aceeasi componenta(adaugarea in cos,filtre)

User story:
As a customer I want to view all electronics products.
As a {user} I want to {action}


