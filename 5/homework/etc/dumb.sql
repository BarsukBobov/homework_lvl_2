--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1 (Debian 16.1-1.pgdg120+1)
-- Dumped by pg_dump version 16.1 (Debian 16.1-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.categories (id, name, parent_id) VALUES (1, 'Электроника', NULL);
INSERT INTO public.categories (id, name, parent_id) VALUES (2, 'Телефоны', 1);
INSERT INTO public.categories (id, name, parent_id) VALUES (3, 'Компьютеры', 1);
INSERT INTO public.categories (id, name, parent_id) VALUES (4, 'Смартфоны', 2);
INSERT INTO public.categories (id, name, parent_id) VALUES (5, 'Ноутбуки', 3);


--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.products (id, name, price, category_id) VALUES (1, 'iPhone X', 100, 4);
INSERT INTO public.products (id, name, price, category_id) VALUES (2, 'Samsung Galaxy S9', 200, 4);
INSERT INTO public.products (id, name, price, category_id) VALUES (3, 'MacBook Pro', 300, 5);
INSERT INTO public.products (id, name, price, category_id) VALUES (4, 'Dell XPS 13', 400, 5);

