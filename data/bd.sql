PGDMP      :                }            deteccion_metales    17.4    17.4 &    G           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            H           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            I           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            J           1262    24672    deteccion_metales    DATABASE     w   CREATE DATABASE deteccion_metales WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'es-ES';
 !   DROP DATABASE deteccion_metales;
                     postgres    false            �            1259    24684    experiments    TABLE     �   CREATE TABLE public.experiments (
    id_experiment integer NOT NULL,
    sensor_id integer NOT NULL,
    experiment_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    description text
);
    DROP TABLE public.experiments;
       public         heap r       postgres    false            �            1259    24683    experiments_id_experiment_seq    SEQUENCE     �   CREATE SEQUENCE public.experiments_id_experiment_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.experiments_id_experiment_seq;
       public               postgres    false    220            K           0    0    experiments_id_experiment_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.experiments_id_experiment_seq OWNED BY public.experiments.id_experiment;
          public               postgres    false    219            �            1259    24699    measurements    TABLE       CREATE TABLE public.measurements (
    id_measurement integer NOT NULL,
    experiment_id integer NOT NULL,
    measurement_time timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    voltage double precision NOT NULL,
    current_avg double precision NOT NULL
);
     DROP TABLE public.measurements;
       public         heap r       postgres    false            �            1259    24698    measurements_id_measurement_seq    SEQUENCE     �   CREATE SEQUENCE public.measurements_id_measurement_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE public.measurements_id_measurement_seq;
       public               postgres    false    222            L           0    0    measurements_id_measurement_seq    SEQUENCE OWNED BY     c   ALTER SEQUENCE public.measurements_id_measurement_seq OWNED BY public.measurements.id_measurement;
          public               postgres    false    221            �            1259    24674    sensors    TABLE       CREATE TABLE public.sensors (
    id_sensor integer NOT NULL,
    name character varying(100) NOT NULL,
    type character varying(50) NOT NULL,
    location character varying(255),
    installation_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    description text
);
    DROP TABLE public.sensors;
       public         heap r       postgres    false            �            1259    24673    sensors_id_sensor_seq    SEQUENCE     �   CREATE SEQUENCE public.sensors_id_sensor_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.sensors_id_sensor_seq;
       public               postgres    false    218            M           0    0    sensors_id_sensor_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.sensors_id_sensor_seq OWNED BY public.sensors.id_sensor;
          public               postgres    false    217            �            1259    24712    users    TABLE     �   CREATE TABLE public.users (
    id_user integer NOT NULL,
    username character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    password text NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public.users;
       public         heap r       postgres    false            �            1259    24711    users_id_user_seq    SEQUENCE     �   CREATE SEQUENCE public.users_id_user_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.users_id_user_seq;
       public               postgres    false    224            N           0    0    users_id_user_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.users_id_user_seq OWNED BY public.users.id_user;
          public               postgres    false    223            �           2604    24687    experiments id_experiment    DEFAULT     �   ALTER TABLE ONLY public.experiments ALTER COLUMN id_experiment SET DEFAULT nextval('public.experiments_id_experiment_seq'::regclass);
 H   ALTER TABLE public.experiments ALTER COLUMN id_experiment DROP DEFAULT;
       public               postgres    false    219    220    220            �           2604    24702    measurements id_measurement    DEFAULT     �   ALTER TABLE ONLY public.measurements ALTER COLUMN id_measurement SET DEFAULT nextval('public.measurements_id_measurement_seq'::regclass);
 J   ALTER TABLE public.measurements ALTER COLUMN id_measurement DROP DEFAULT;
       public               postgres    false    222    221    222            �           2604    24677    sensors id_sensor    DEFAULT     v   ALTER TABLE ONLY public.sensors ALTER COLUMN id_sensor SET DEFAULT nextval('public.sensors_id_sensor_seq'::regclass);
 @   ALTER TABLE public.sensors ALTER COLUMN id_sensor DROP DEFAULT;
       public               postgres    false    218    217    218            �           2604    24715    users id_user    DEFAULT     n   ALTER TABLE ONLY public.users ALTER COLUMN id_user SET DEFAULT nextval('public.users_id_user_seq'::regclass);
 <   ALTER TABLE public.users ALTER COLUMN id_user DROP DEFAULT;
       public               postgres    false    224    223    224            @          0    24684    experiments 
   TABLE DATA           ]   COPY public.experiments (id_experiment, sensor_id, experiment_date, description) FROM stdin;
    public               postgres    false    220   �-       B          0    24699    measurements 
   TABLE DATA           m   COPY public.measurements (id_measurement, experiment_id, measurement_time, voltage, current_avg) FROM stdin;
    public               postgres    false    222   �-       >          0    24674    sensors 
   TABLE DATA           b   COPY public.sensors (id_sensor, name, type, location, installation_date, description) FROM stdin;
    public               postgres    false    218   �-       D          0    24712    users 
   TABLE DATA           O   COPY public.users (id_user, username, email, password, created_at) FROM stdin;
    public               postgres    false    224   �-       O           0    0    experiments_id_experiment_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.experiments_id_experiment_seq', 1, false);
          public               postgres    false    219            P           0    0    measurements_id_measurement_seq    SEQUENCE SET     N   SELECT pg_catalog.setval('public.measurements_id_measurement_seq', 1, false);
          public               postgres    false    221            Q           0    0    sensors_id_sensor_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.sensors_id_sensor_seq', 1, false);
          public               postgres    false    217            R           0    0    users_id_user_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.users_id_user_seq', 1, false);
          public               postgres    false    223            �           2606    24692    experiments experiments_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.experiments
    ADD CONSTRAINT experiments_pkey PRIMARY KEY (id_experiment);
 F   ALTER TABLE ONLY public.experiments DROP CONSTRAINT experiments_pkey;
       public                 postgres    false    220            �           2606    24705    measurements measurements_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.measurements
    ADD CONSTRAINT measurements_pkey PRIMARY KEY (id_measurement);
 H   ALTER TABLE ONLY public.measurements DROP CONSTRAINT measurements_pkey;
       public                 postgres    false    222            �           2606    24682    sensors sensors_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.sensors
    ADD CONSTRAINT sensors_pkey PRIMARY KEY (id_sensor);
 >   ALTER TABLE ONLY public.sensors DROP CONSTRAINT sensors_pkey;
       public                 postgres    false    218            �           2606    24722    users users_email_key 
   CONSTRAINT     Q   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);
 ?   ALTER TABLE ONLY public.users DROP CONSTRAINT users_email_key;
       public                 postgres    false    224            �           2606    24720    users users_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id_user);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public                 postgres    false    224            �           1259    24724    idx_experiment_sensor    INDEX     R   CREATE INDEX idx_experiment_sensor ON public.experiments USING btree (sensor_id);
 )   DROP INDEX public.idx_experiment_sensor;
       public                 postgres    false    220            �           1259    24725    idx_measurements_experiment    INDEX     ]   CREATE INDEX idx_measurements_experiment ON public.measurements USING btree (experiment_id);
 /   DROP INDEX public.idx_measurements_experiment;
       public                 postgres    false    222            �           1259    24723    idx_sensor_name    INDEX     C   CREATE INDEX idx_sensor_name ON public.sensors USING btree (name);
 #   DROP INDEX public.idx_sensor_name;
       public                 postgres    false    218            �           2606    24693 &   experiments experiments_sensor_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.experiments
    ADD CONSTRAINT experiments_sensor_id_fkey FOREIGN KEY (sensor_id) REFERENCES public.sensors(id_sensor) ON DELETE CASCADE;
 P   ALTER TABLE ONLY public.experiments DROP CONSTRAINT experiments_sensor_id_fkey;
       public               postgres    false    218    220    4767            �           2606    24706 ,   measurements measurements_experiment_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.measurements
    ADD CONSTRAINT measurements_experiment_id_fkey FOREIGN KEY (experiment_id) REFERENCES public.experiments(id_experiment) ON DELETE CASCADE;
 V   ALTER TABLE ONLY public.measurements DROP CONSTRAINT measurements_experiment_id_fkey;
       public               postgres    false    4769    222    220            @      x������ � �      B      x������ � �      >      x������ � �      D      x������ � �     