# calc.kinship — родство по конечному графу

Каталог [P28](../../../../docs/catalogs/COMPUTATIONAL-PRIMITIVES-CATALOG.ru.md#p28);
заведён по [DECISION-0206](../../../../spec/decisions/0206-primitives-queue-for-kz-corpus.ru.md)
пункт 5 и [DECISION-0217](../../../../spec/decisions/0217-calc-kinship-inheritance.ru.md).

## Что делает

Вход — `Family`: `parent_edge(f, parent, child, Blood|Adoptive)`,
`spouse_edge`, `family_degree_count(Roman|Canonical)`,
`family_adoption_effect(ReplacesBlood|AddsBranch)`, `family_depth_cap`.
Лица — стандартный `Actor`: лица хабов (ГК РК `Person : CivilParticipant : Actor`)
принимаются без сущности-двойника.

Выход: `effective_parent`, `ancestor_or_self(f, a, p, depth)`, `spouses`,
`kin_degree` (наименьшая по общим предкам), `kin_line`
(`Ascending`/`Descending`/`Collateral`), `full_sibling`/`half_sibling`/`sibling`,
`parent`/`child`/`grandparent`/`grandchild`/`great_grandparent`,
`uncle_or_aunt`/`nephew_or_niece`/`cousin`, `cousin_grandchild`,
`great_uncle_or_aunt`, `cousin_great_grandchild`, `cousin_nephew_or_niece`,
`cousin_uncle_or_aunt`; дефекты `family_defect` по имени.

## Три свойства

1. **Политики входом, умолчаний нет.** Римский счёт — сумма глубин до общего
   предка, канонический — большая из них; усыновление — заменяет кровную
   ветвь (ГК РК) или добавляет.
2. **Тождество лиц — глубина 0.** Неравенство сущностей в теле правила
   недоступно; «разные лица» — счёт `ancestor_or_self(f, a, b, 0)` нулём.
3. **Рекурсия ограничена входом.** Предки считаются до `family_depth_cap`;
   цикл в данных — названный дефект `CycleDetected`, а не зависание.

## Чего пакет не знает

Кто наследует, кому запрещён брак, кто «близкий родственник» в конкретном
законе, свойство и его прекращение. Потребитель объявляет это правилами со
своим `@source`.

## Потребитель

`kz.corpus.civilcode_inheritance`, статьи 1060–1064: модуль
`07-rodstvo-po-grafu.law` подаёт граф семьи наследодателя, объявляет
«усыновление заменяет» нормой пункта 2 статьи 1060 и выводит плоские факты
родства очередей 1–6 из графа; семейство `#kinship` — 8 тестов, обе
реализации байтово.

## Проверка

39 сценариев `tests/calc-kinship.lawtest` (семейство `calc_kinship`) на одной
семье четырёх поколений. `check_primitives.py --only kinship`: обе реализации,
байтово 39/39 (13.09.2026).
