<?xml version="1.0" encoding="UTF-8"?>

<!-- TRANSFORMATION POUR AFFICHER LES RESULTATS CHANSONS PAR DIALECTES -->

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

    <!-- ***********************************************************     -->
    <!-- Version 1                                                       -->
    <!-- Ce script                                                       -->
    <!-- a été développé dans le cadre du projet                         -->
    <!-- Open Barzaz Breiz Collection                                    -->
    <!-- ***********************************************************     -->
    <!-- Author :                                                        -->
    <!-- @Github- Lucaterre                                              -->
    <!-- ***********************************************************     -->
    <!-- Ce script est libre à la réutilisation selon les termes         -->
    <!-- de la Creative Commons Attribution license.                     -->
    <!-- ***********************************************************     -->

    <xsl:output method="html" indent="yes"/>
    <xsl:param name="dialecteXsl"/>

    <xsl:variable name="cheminDialecte" select="//body/div/div[@type = 'D'][@n = $dialecteXsl]"/>

    <!-- HTML -->

    <xsl:template match="/">
        <h3 style="text-align: center;">
            <xsl:text/>
            <xsl:value-of select="$cheminDialecte/head"/>
            <xsl:text/>
        </h3>
        <br/>
        <xsl:for-each select="$cheminDialecte/div[@type = 'chanson']">
            <li class="titre-resdialectes">
                <a class="titre-resDialectes">
                    <xsl:attribute name="href">
                        <xsl:text>affichage/</xsl:text>
                        <xsl:value-of select="@n"/>
                    </xsl:attribute>
                    <xsl:attribute name="target">_blank</xsl:attribute>
                    <xsl:value-of select="head"/>
                </a>
            </li>
            <hr/>
        </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>
