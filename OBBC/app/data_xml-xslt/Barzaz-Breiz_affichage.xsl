<?xml version="1.0" encoding="UTF-8"?>


<!-- TRANSFORMATION POUR L'AFFICHAGE DES CHANSONS -->

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0">
    <xsl:output method="html" indent="yes"/>
    <xsl:param name="numero"/>


    <!-- variable -->
    <xsl:variable name="chemin_chanson" select="descendant::div[@type = 'chanson'][@n = $numero]"/>


    <!-- HTML -->

    <xsl:template match="/">
        <br/>
        <h2>
            <xsl:text/>
            <xsl:value-of select="$chemin_chanson/head[@type = 'titre_général']"/>
            <!-- titre général de la page -->
            <xsl:text/>
        </h2>
        <hr/>
        <div>
            <h4>
                <xsl:value-of select="$chemin_chanson/ancestor::div[@type = 'D']/head/text()"/>
            </h4>
            <!-- dialecte chanson -->
        </div>
        <hr/>
        <br/>
        <div class="shadow p-3 mb-5 bg-white rounded argument">
            <!-- template argument -->
            <section>
                <xsl:apply-templates select="$chemin_chanson/div[@type = 'argument']"/>
            </section>
        </div>
        <hr/>
        <div class="container">
            <div class="row">
                <div class="col">
                    <xsl:apply-templates select="$chemin_chanson/div[@type = 'transcription']"/>
                    <!-- div pour la transcription -->
                </div>
                <div class="col">
                    <!-- div pour le texte original -->
                    <xsl:apply-templates select="$chemin_chanson/div[@type = 'original']"/>
                </div>
            </div>
        </div>
        <hr/>
        <br/>
        <div class="shadow p-3 mb-5 bg-white rounded Ne">
            <!-- template notes et éclaircissements -->
            <section>
                <xsl:apply-templates select="$chemin_chanson/div[@type = 'Ne']"/>
            </section>
        </div>
        <a class="btn btn-affichage" target="_blank">
            <xsl:attribute name="href">
                <xsl:text>download/</xsl:text>
                <xsl:value-of select="$numero"/>
            </xsl:attribute>
            <xsl:text>Affichage du code XML/TEI</xsl:text>
        </a>
    </xsl:template>

    <!--________________________-->

    <!-- template pour l'argument -->

    <xsl:template match="div[@type = 'argument']">
        <h4>
            <xsl:copy-of select="head/text()"/>
        </h4>
        <xsl:copy-of select="p"/>
    </xsl:template>

    <!--_________________________ -->

    <!-- templates pour la transcription française -->

    <xsl:template match="div[@type = 'transcription']">
        <h4>
            <xsl:value-of
                select="$chemin_chanson/div[@type = 'transcription']/head[@type = 'titre-français']"
            />
        </h4>
        <xsl:apply-templates select="lg"/>
    </xsl:template>

    <!--_________________________ -->

    <!-- templates pour l'original -->

    <xsl:template match="div[@type = 'original']">
        <h4>
            <xsl:value-of select="head[@type = 'titre-breton']"/>
        </h4>
        <xsl:apply-templates select="lg"/>
    </xsl:template>

    <!--_________________________ -->

    <!-- template pour les notes et éclairssissements -->

    <xsl:template match="//div[@type = 'Ne']">
        <h4>
            <xsl:value-of select="head/text()"/>
        </h4>
        <xsl:copy-of select="div | p | lg | l"/>
    </xsl:template>

    <xsl:template match="p">
        <xsl:copy-of select="."/>
    </xsl:template>

    <xsl:template match="lg">
        <div class="scroll-div">
            <xsl:apply-templates select="l"/>
        </div>
    </xsl:template>

    <xsl:template match="l">
        <p>
            <xsl:number count="l" format="1" level="single"/>
            <xsl:text>. </xsl:text>
            <xsl:value-of select="."/>
        </p>
    </xsl:template>


    <!--_________________________ -->

</xsl:stylesheet>
