-- Run MySQL Script in WorkBench to create required tables automatically

-- -----------------------------------------------------
-- Schema store
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS "store" ;

-- -----------------------------------------------------
-- Schema store
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS "store";
--USE "store";

-- -----------------------------------------------------
-- Table "store"."member"
-- -----------------------------------------------------
DROP TABLE IF EXISTS "store"."member" ;

CREATE TABLE IF NOT EXISTS "store"."member" (
  "member_id" UUID NOT NULL,
  "member_name" VARCHAR(50) NOT NULL,
  "member_password" UUID NOT NULL,
  "member_bonus_points" FLOAT NOT NULL,
  "member_created_date" TIMESTAMP NOT NULL,
  "member_updated_date" TIMESTAMP NOT NULL,
  PRIMARY KEY ("member_id"));


-- -----------------------------------------------------
-- Table "store"."member_level"
-- -----------------------------------------------------
DROP TABLE IF EXISTS "store"."member_level" ;

CREATE TABLE IF NOT EXISTS "store"."member_level" (
  "member_level_id" UUID NOT NULL,
  "member_level" VARCHAR(50) NOT NULL,
  "bonus_points_min" FLOAT NOT NULL,
  "bonus_points_max" FLOAT NOT NULL,
  "member_level_created_date" TIMESTAMP NOT NULL,
  "member_level_updated_date" TIMESTAMP NOT NULL,
  PRIMARY KEY ("member_level_id"));


-- -----------------------------------------------------
-- Table "store"."order"
-- -----------------------------------------------------
DROP TABLE IF EXISTS "store"."order" ;

CREATE TABLE IF NOT EXISTS "store"."order" (
  "order_id" UUID NOT NULL,
  "member_id" UUID NOT NULL,
  "order_created_date" TIMESTAMP NOT NULL,
  "order_updated_date" TIMESTAMP NOT NULL,
  PRIMARY KEY ("order_id"),
  CONSTRAINT "order_fk0"
    FOREIGN KEY ("member_id")
    REFERENCES "store"."member" ("member_id")
    ON DELETE RESTRICT
    ON UPDATE RESTRICT);


-- -----------------------------------------------------
-- Table "store"."uom"
-- -----------------------------------------------------
DROP TABLE IF EXISTS "store"."uom" ;

CREATE TABLE IF NOT EXISTS "store"."uom" (
  "uom_id" UUID NOT NULL,
  "uom_name" VARCHAR(50) NOT NULL,
  "uom_created_date" TIMESTAMP NOT NULL,
  "uom_updated_date" TIMESTAMP NOT NULL,
  PRIMARY KEY ("uom_id"));


-- -----------------------------------------------------
-- Table "store"."product"
-- -----------------------------------------------------
DROP TABLE IF EXISTS "store"."product" ;

CREATE TABLE IF NOT EXISTS "store"."product" (
  "product_id" UUID NOT NULL,
  "product_name" VARCHAR(50) NOT NULL,
  "uom_id" UUID NOT NULL,
  "product_unit_price" FLOAT NOT NULL,
  "product_bonus_points" FLOAT NOT NULL,
  "product_created_date" TIMESTAMP NOT NULL,
  "product_updated_date" TIMESTAMP NOT NULL,
  PRIMARY KEY ("product_id"),
  CONSTRAINT "product_fk0"
    FOREIGN KEY ("uom_id")
    REFERENCES "store"."uom" ("uom_id")
    ON DELETE RESTRICT
    ON UPDATE RESTRICT);


-- -----------------------------------------------------
-- Table "store"."order_item"
-- -----------------------------------------------------
DROP TABLE IF EXISTS "store"."order_item" ;

CREATE TABLE IF NOT EXISTS "store"."order_item" (
  "order_item_id" UUID NOT NULL,
  "order_id" UUID NOT NULL,
  "product_id" UUID NOT NULL,
  "order_item_quantity" FLOAT NOT NULL,
  "order_item_created_date" TIMESTAMP NOT NULL,
  "order_item_updated_date" TIMESTAMP NOT NULL,
  PRIMARY KEY ("order_item_id"),
  CONSTRAINT "order_item_fk0"
    FOREIGN KEY ("order_id")
    REFERENCES "store"."order" ("order_id"),
  CONSTRAINT "order_item_fk1"
    FOREIGN KEY ("product_id")
    REFERENCES "store"."product" ("product_id")
    ON DELETE RESTRICT
    ON UPDATE RESTRICT);
