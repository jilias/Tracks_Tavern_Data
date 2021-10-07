-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

DROP TABLE "sales";
DROP TABLE "weather";

CREATE TABLE "sales" (
	"index" int not null,
    "item" varchar   NOT NULL,
    "item_code" int   NOT NULL,
    "quantity" int   NOT NULL,
    "unit_price" float   NOT NULL,
    "total_sales_amount" float   NOT NULL,
    "date" date   NOT NULL,
    "Type" varchar   NOT NULL
);

CREATE TABLE "weather" (
	"index" int not null,
    "dt" date PRIMARY KEY,
    "temp" float   NOT NULL,
    "feels_like" float   NOT NULL,
    "temp_min" float   NOT NULL,
    "temp_max" float   NOT NULL,
    "pressure" float   NOT NULL,
    "humidity" float   NOT NULL,
    "wind_speed" float   NOT NULL,
    "clouds_all" float   NOT NULL,
    "weather_main_Clear" float   NOT NULL,
    "weather_main_Clouds" float   NOT NULL,
    "weather_main_Drizzle" float   NOT NULL,
    "weather_main_Fog" float   NOT NULL,
    "weather_main_Haze" float   NOT NULL,
	"weather_main_Mist" float NOT NULL,
    "weather_main_Rain" float   NOT NULL,
    "weather_main_Smoke" float   NOT NULL,
    "weather_main_Snow" float   NOT NULL,
	"weather_main_Thunderstorm" float NOT NULL
);