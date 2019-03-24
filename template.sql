CREATE DATABASE gpolymath;

CREATE TABLE professionals (
    person_id           INT             PRIMARY KEY AUTO_INCREMENT,
    person_name         VARCHAR(50)     NOT NULL,
    position            VARCHAR(50),
    birth_year          VARCHAR(5),
    hometown            VARCHAR(50),
    current_location    VARCHAR(50),
    sexual_orientation  VARCHAR(15),
    website             VARCHAR(50),
    twitter             VARCHAR(50),
    facebook            VARCHAR(50),
    youtube             VARCHAR(50),
    github              VARCHAR(50),
    media_uploads       VARCHAR(200)
);

CREATE TABLE articles (
    article_id          INT             PRIMARY KEY AUTO_INCREMENT,
    title               VARCHAR(100)    NOT NULL,
    tags                VARCHAR(200)    NOT NULL,
    question            VARCHAR(200),
    link_paper          VARCHAR(100)    NOT NULL,
    link_news           VARCHAR(100)
);

CREATE TABLE tags (
    tag_id              INT             PRIMARY KEY AUTO_INCREMENT,
    tag_name            VARCHAR(50)
);

CREATE TABLE links_tags_articles (
    tag_id              INT             NOT NULL,
    article_id          INT             NOT NULL,
    CONSTRAINT tag_id_fn
        FOREIGN KEY (tag_id)
        REFERENCES tags (tag_id),
    CONSTRAINT article_id_fn
        FOREIGN KEY (article_id)
        REFERENCES articles (article_id)
);

CREATE TABLE links_professionals_articles (
    person_id           INT             NOT NULL,
    article_id          INT             NOT NULL,
    CONSTRAINT person_id_fn
        FOREIGN KEY (person_id)
        REFERENCES professionals (person_id),
    CONSTRAINT article_id_fn
        FOREIGN KEY (article_id)
        REFERENCES articles (article_id)
);