--
-- PostgreSQL database dump
--

-- Dumped from database version 17.4
-- Dumped by pg_dump version 17.4

-- Started on 2025-03-20 13:29:58

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4938 (class 1262 OID 24672)
-- Name: deteccion_metales; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE deteccion_metales WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'es-ES';


ALTER DATABASE deteccion_metales OWNER TO postgres;

\connect deteccion_metales

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 220 (class 1259 OID 24684)
-- Name: experiments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.experiments (
    id_experiment integer NOT NULL,
    sensor_id integer NOT NULL,
    experiment_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    description text
);


ALTER TABLE public.experiments OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 24683)
-- Name: experiments_id_experiment_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.experiments_id_experiment_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.experiments_id_experiment_seq OWNER TO postgres;

--
-- TOC entry 4939 (class 0 OID 0)
-- Dependencies: 219
-- Name: experiments_id_experiment_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.experiments_id_experiment_seq OWNED BY public.experiments.id_experiment;


--
-- TOC entry 222 (class 1259 OID 24699)
-- Name: measurements; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.measurements (
    id_measurement integer NOT NULL,
    experiment_id integer NOT NULL,
    measurement_time timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    voltage double precision NOT NULL,
    current_avg double precision NOT NULL
);


ALTER TABLE public.measurements OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 24698)
-- Name: measurements_id_measurement_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.measurements_id_measurement_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.measurements_id_measurement_seq OWNER TO postgres;

--
-- TOC entry 4940 (class 0 OID 0)
-- Dependencies: 221
-- Name: measurements_id_measurement_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.measurements_id_measurement_seq OWNED BY public.measurements.id_measurement;


--
-- TOC entry 218 (class 1259 OID 24674)
-- Name: sensors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sensors (
    id_sensor integer NOT NULL,
    name character varying(100) NOT NULL,
    type character varying(50) NOT NULL,
    location character varying(255),
    installation_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    description text
);


ALTER TABLE public.sensors OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 24673)
-- Name: sensors_id_sensor_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sensors_id_sensor_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sensors_id_sensor_seq OWNER TO postgres;

--
-- TOC entry 4941 (class 0 OID 0)
-- Dependencies: 217
-- Name: sensors_id_sensor_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sensors_id_sensor_seq OWNED BY public.sensors.id_sensor;


--
-- TOC entry 224 (class 1259 OID 24712)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id_user integer NOT NULL,
    username character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    password text NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 24711)
-- Name: users_id_user_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_user_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_user_seq OWNER TO postgres;

--
-- TOC entry 4942 (class 0 OID 0)
-- Dependencies: 223
-- Name: users_id_user_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_user_seq OWNED BY public.users.id_user;


--
-- TOC entry 4759 (class 2604 OID 24687)
-- Name: experiments id_experiment; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.experiments ALTER COLUMN id_experiment SET DEFAULT nextval('public.experiments_id_experiment_seq'::regclass);


--
-- TOC entry 4761 (class 2604 OID 24702)
-- Name: measurements id_measurement; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.measurements ALTER COLUMN id_measurement SET DEFAULT nextval('public.measurements_id_measurement_seq'::regclass);


--
-- TOC entry 4757 (class 2604 OID 24677)
-- Name: sensors id_sensor; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sensors ALTER COLUMN id_sensor SET DEFAULT nextval('public.sensors_id_sensor_seq'::regclass);


--
-- TOC entry 4763 (class 2604 OID 24715)
-- Name: users id_user; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id_user SET DEFAULT nextval('public.users_id_user_seq'::regclass);


--
-- TOC entry 4928 (class 0 OID 24684)
-- Dependencies: 220
-- Data for Name: experiments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.experiments (id_experiment, sensor_id, experiment_date, description) FROM stdin;
\.


--
-- TOC entry 4930 (class 0 OID 24699)
-- Dependencies: 222
-- Data for Name: measurements; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.measurements (id_measurement, experiment_id, measurement_time, voltage, current_avg) FROM stdin;
\.


--
-- TOC entry 4926 (class 0 OID 24674)
-- Dependencies: 218
-- Data for Name: sensors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sensors (id_sensor, name, type, location, installation_date, description) FROM stdin;
\.


--
-- TOC entry 4932 (class 0 OID 24712)
-- Dependencies: 224
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id_user, username, email, password, created_at) FROM stdin;
\.


--
-- TOC entry 4943 (class 0 OID 0)
-- Dependencies: 219
-- Name: experiments_id_experiment_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.experiments_id_experiment_seq', 1, false);


--
-- TOC entry 4944 (class 0 OID 0)
-- Dependencies: 221
-- Name: measurements_id_measurement_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.measurements_id_measurement_seq', 1, false);


--
-- TOC entry 4945 (class 0 OID 0)
-- Dependencies: 217
-- Name: sensors_id_sensor_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sensors_id_sensor_seq', 1, false);


--
-- TOC entry 4946 (class 0 OID 0)
-- Dependencies: 223
-- Name: users_id_user_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_user_seq', 1, false);


--
-- TOC entry 4769 (class 2606 OID 24692)
-- Name: experiments experiments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.experiments
    ADD CONSTRAINT experiments_pkey PRIMARY KEY (id_experiment);


--
-- TOC entry 4773 (class 2606 OID 24705)
-- Name: measurements measurements_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.measurements
    ADD CONSTRAINT measurements_pkey PRIMARY KEY (id_measurement);


--
-- TOC entry 4767 (class 2606 OID 24682)
-- Name: sensors sensors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sensors
    ADD CONSTRAINT sensors_pkey PRIMARY KEY (id_sensor);


--
-- TOC entry 4775 (class 2606 OID 24722)
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- TOC entry 4777 (class 2606 OID 24720)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id_user);


--
-- TOC entry 4770 (class 1259 OID 24724)
-- Name: idx_experiment_sensor; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_experiment_sensor ON public.experiments USING btree (sensor_id);


--
-- TOC entry 4771 (class 1259 OID 24725)
-- Name: idx_measurements_experiment; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_measurements_experiment ON public.measurements USING btree (experiment_id);


--
-- TOC entry 4765 (class 1259 OID 24723)
-- Name: idx_sensor_name; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_sensor_name ON public.sensors USING btree (name);


--
-- TOC entry 4778 (class 2606 OID 24693)
-- Name: experiments experiments_sensor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.experiments
    ADD CONSTRAINT experiments_sensor_id_fkey FOREIGN KEY (sensor_id) REFERENCES public.sensors(id_sensor) ON DELETE CASCADE;


--
-- TOC entry 4779 (class 2606 OID 24706)
-- Name: measurements measurements_experiment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.measurements
    ADD CONSTRAINT measurements_experiment_id_fkey FOREIGN KEY (experiment_id) REFERENCES public.experiments(id_experiment) ON DELETE CASCADE;


-- Completed on 2025-03-20 13:29:59

--
-- PostgreSQL database dump complete
--

