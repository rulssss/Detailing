PGDMP      1    	            |            tiziano    16.3    16.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    24822    tiziano    DATABASE     ~   CREATE DATABASE tiziano WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Argentina.1252';
    DROP DATABASE tiziano;
                postgres    false            �            1259    24835    jobs    TABLE     !  CREATE TABLE public.jobs (
    work_completed_id integer NOT NULL,
    client character varying(20) NOT NULL,
    year integer NOT NULL,
    car character varying(20) NOT NULL,
    job integer NOT NULL,
    month integer NOT NULL,
    amount integer NOT NULL,
    cost integer NOT NULL
);
    DROP TABLE public.jobs;
       public         heap    postgres    false            �            1259    24846    jobs_work_completed_id_seq    SEQUENCE     �   CREATE SEQUENCE public.jobs_work_completed_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.jobs_work_completed_id_seq;
       public          postgres    false    216            �           0    0    jobs_work_completed_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.jobs_work_completed_id_seq OWNED BY public.jobs.work_completed_id;
          public          postgres    false    218            �            1259    24832 	   type_jobs    TABLE     h   CREATE TABLE public.type_jobs (
    job_id integer NOT NULL,
    name character varying(30) NOT NULL
);
    DROP TABLE public.type_jobs;
       public         heap    postgres    false            �            1259    24838    type_jobs_job_id_seq    SEQUENCE     �   CREATE SEQUENCE public.type_jobs_job_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.type_jobs_job_id_seq;
       public          postgres    false    215            �           0    0    type_jobs_job_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.type_jobs_job_id_seq OWNED BY public.type_jobs.job_id;
          public          postgres    false    217                        2604    24847    jobs work_completed_id    DEFAULT     �   ALTER TABLE ONLY public.jobs ALTER COLUMN work_completed_id SET DEFAULT nextval('public.jobs_work_completed_id_seq'::regclass);
 E   ALTER TABLE public.jobs ALTER COLUMN work_completed_id DROP DEFAULT;
       public          postgres    false    218    216                       2604    24839    type_jobs job_id    DEFAULT     t   ALTER TABLE ONLY public.type_jobs ALTER COLUMN job_id SET DEFAULT nextval('public.type_jobs_job_id_seq'::regclass);
 ?   ALTER TABLE public.type_jobs ALTER COLUMN job_id DROP DEFAULT;
       public          postgres    false    217    215            �          0    24835    jobs 
   TABLE DATA           ^   COPY public.jobs (work_completed_id, client, year, car, job, month, amount, cost) FROM stdin;
    public          postgres    false    216   �       �          0    24832 	   type_jobs 
   TABLE DATA           1   COPY public.type_jobs (job_id, name) FROM stdin;
    public          postgres    false    215   y       �           0    0    jobs_work_completed_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.jobs_work_completed_id_seq', 394, true);
          public          postgres    false    218            �           0    0    type_jobs_job_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.type_jobs_job_id_seq', 14, true);
          public          postgres    false    217            &           2606    24849    jobs jobs_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.jobs
    ADD CONSTRAINT jobs_pkey PRIMARY KEY (work_completed_id);
 8   ALTER TABLE ONLY public.jobs DROP CONSTRAINT jobs_pkey;
       public            postgres    false    216            "           2606    25270    type_jobs type_jobs_name_key 
   CONSTRAINT     W   ALTER TABLE ONLY public.type_jobs
    ADD CONSTRAINT type_jobs_name_key UNIQUE (name);
 F   ALTER TABLE ONLY public.type_jobs DROP CONSTRAINT type_jobs_name_key;
       public            postgres    false    215            $           2606    24841    type_jobs type_jobs_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.type_jobs
    ADD CONSTRAINT type_jobs_pkey PRIMARY KEY (job_id);
 B   ALTER TABLE ONLY public.type_jobs DROP CONSTRAINT type_jobs_pkey;
       public            postgres    false    215            '           2606    24859    jobs jobs_job_fkey    FK CONSTRAINT     u   ALTER TABLE ONLY public.jobs
    ADD CONSTRAINT jobs_job_fkey FOREIGN KEY (job) REFERENCES public.type_jobs(job_id);
 <   ALTER TABLE ONLY public.jobs DROP CONSTRAINT jobs_job_fkey;
       public          postgres    false    216    215    4644            �   �   x��н� ���0��ZxG�bmĒPZ�O�mI����p�/'� ���	�<p�%\|hAA��
JB�__4{w��CI+�i�c�����;K�߀a��Sc
�(B�"MT�)�a�`��j>L��/45�)WӍ�L�]Ѻ%ے ��T@�_��wiGN+��u�G�?�yGy�!|�      �   Z   x��;�  й=�' �z�M
%|9�0��R��$����B�7�߀ᐘ�[<-�A�A�4v�B�h�Ge��yV�"����     