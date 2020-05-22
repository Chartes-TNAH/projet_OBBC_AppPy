<?xml version="1.0" encoding="UTF-8"?>

<!-- TRANSFORMATION POUR AFFICHER LES RESULTATS CHANSONS PAR THEMES -->

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
    <xsl:param name="themeXsl"/>

    <xsl:variable name="cheminTheme" select="//body/div[@type = 'T'][@n = $themeXsl]"/>

    <!-- HTML -->

    <xsl:template match="/">
        <h3 style="text-align: center;">
            <xsl:text/>
            <xsl:value-of select="$cheminTheme/head"/>
            <xsl:text/>
        </h3>
        <br/>
        <xsl:for-each select="$cheminTheme/div/div['chanson']">
            <li class="titre-resthemes">
                <a class="titre-resthemes">
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
