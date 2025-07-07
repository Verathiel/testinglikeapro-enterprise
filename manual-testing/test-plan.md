# Test Plan – OrangeHRM Enterprise QA Project

## Cíl testování
Ověřit funkčnost, stabilitu, použitelnost a bezpečnost základních modulů OrangeHRM demo systému. Testujeme reálný systém jako simulaci podnikového QA procesu.

## Rozsah testování
- Login a autentizace
- Role-based přístupy
- Moduly: Dashboard, Employee List, Leave Management, User Management
- Formuláře a validace
- Chybová hlášení
- Zabezpečení (basic)
- Přístupnost (WCAG základ)

## Typy testů
- Ruční testování základních toků
- Automatizované UI testy (Selenium)
- API testy (Postman, Python)
- CI/CD testovací pipeline
- Přístupnost a bezpečnostní edge casy

## Nástroje
- Selenium (Python)
- Postman / Python requests
- GitHub Actions
- axe-core (přístupnost)
- Linux + Browser DevTools

## Předpoklady
- Přístup do OrangeHRM demo: https://opensource-demo.orangehrmlive.com/
- Login: `Admin`, Password: `admin123`
- Stabilní síť, Chrome nebo Firefox

## Časový rámec
- Fáze 1: Ruční testování – 3 dny
- Fáze 2: Automatizace – 5 dní
- Fáze 3: API + CI/CD – 3 dny
- Fáze 4: Pokročilé testy + dokumentace – 3 dny
