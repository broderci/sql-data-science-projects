COMMENT ON TABLE person_discounts IS 'discounts for persons';

COMMENT ON COLUMN person_discounts.id IS 'primary key identifier';

COMMENT ON COLUMN person_discounts.person_id IS 'person identifier';

COMMENT ON COLUMN person_discounts.pizzeria_id IS 'pizzeria identifier';

COMMENT ON COLUMN person_discounts.discount IS 'percent discount fo the client';
