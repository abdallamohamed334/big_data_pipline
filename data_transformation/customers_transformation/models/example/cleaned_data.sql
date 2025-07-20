with base as (
    select
        id,
        name,
        address,
        city_name,
        phone,
        card_number
    from {{ source('raw', 'customer_raw') }}
),

cleaned as (
    select
        id,
        initcap(trim(name)) as clean_name,
        trim(address) as clean_address,
        trim(city_name) as clean_city,
        regexp_replace(regexp_replace(phone, 'x.*$', ''), '[^0-9]', '', 'g') as clean_phone,
        regexp_replace(card_number, '[^0-9]', '', 'g') as clean_card_number,
        current_timestamp as load_timestamp  -- هنا عمود توقيت الإضافة
    from base
)

select * from cleaned
