-- marketing_sql_tasks.sql
-- SQLite queries for diplom ishi (marketing kampaniyalari tahlili)

-- 23. Qaysi kampaniyalar eng ko‘p daromad keltirdi va qaysilari zarar keltirdi?
-- Bu yerda campaign_performance jadvalidagi revenue_uzs va cost_uzs dan foydalangan holda
-- har bir kampaniya bo‘yicha umumiy daromad, xarajat va foyda/zarar hisoblanadi.

SELECT
    c.campaign_id,
    c.campaign_name,
    SUM(p.revenue_uzs) AS total_revenue_uzs,
    SUM(p.cost_uzs)    AS total_cost_uzs,
    SUM(p.revenue_uzs) - SUM(p.cost_uzs) AS profit_uzs
FROM campaign_performance AS p
JOIN campaigns AS c
    ON p.campaign_id = c.campaign_id
GROUP BY c.campaign_id, c.campaign_name
ORDER BY profit_uzs DESC;


-- 25. Qaysi demografik guruhlar marketing kampaniyalariga eng yaxshi javob beradi?
-- Bu yerda customers_acquired jadvalidagi age_group va gender kesimida
-- o‘rtacha LTV va birinchi xarid asosida segment samaradorligi baholanadi.

SELECT
    age_group,
    LOWER(gender) AS gender_norm,
    COUNT(*)                       AS customers_count,
    AVG(first_purchase_amount)     AS avg_first_purchase_uzs,
    AVG(lifetime_value)            AS avg_ltv_uzs
FROM customers_acquired
GROUP BY age_group, gender_norm
ORDER BY avg_ltv_uzs DESC;


-- 29. Fasliy kampaniyalar (bayramlar, chegirmalar) samaradorligi qanday?
-- Faraz qilamiz: campaigns jadvalidagi campaign_type ustunida
-- 'Seasonal', 'Holiday', 'Discount' kabi qiymatlar bor.
-- Ushbu so‘rov fasliy kampaniyalar bo‘yicha ROAS hisoblaydi.

SELECT
    c.campaign_type,
    c.campaign_id,
    c.campaign_name,
    SUM(p.revenue_uzs) AS total_revenue_uzs,
    SUM(p.cost_uzs)    AS total_cost_uzs,
    CASE
        WHEN SUM(p.cost_uzs) > 0 THEN
            SUM(p.revenue_uzs) * 1.0 / SUM(p.cost_uzs)
        ELSE NULL
    END AS roas
FROM campaign_performance AS p
JOIN campaigns AS c
    ON p.campaign_id = c.campaign_id
WHERE LOWER(c.campaign_type) IN ('seasonal', 'holiday', 'discount')
GROUP BY c.campaign_type, c.campaign_id, c.campaign_name
ORDER BY roas DESC;


-- 33. Organic traffic va paid traffic o‘rtasidagi farq va samaradorligi.
-- Faraz qilamiz: customers_acquired jadvalidagi source ustunida
-- 'organic' va 'paid' kabi manbalar bor.

SELECT
    LOWER(source) AS source_type,
    COUNT(*)                   AS customers_count,
    AVG(first_purchase_amount) AS avg_first_purchase_uzs,
    AVG(lifetime_value)        AS avg_ltv_uzs
FROM customers_acquired
GROUP BY source_type
ORDER BY avg_ltv_uzs DESC;

