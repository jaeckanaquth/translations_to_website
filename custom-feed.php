<?php
/**
 * Novel Feed Generator
 * 
 * @package TranslationsToWebsite
 * @version 1.0.0
 */

// Feed configuration constants
define('FEED_ITEMS_LIMIT', 50);

function generate_novel_feed() {
    /**
     * Generate RSS feed for translated novel chapters
     */

// Disable caching
header('Cache-Control: no-cache, must-revalidate');
header('Expires: Mon, 26 Jul 1997 05:00:00 GMT');
header('Content-Type: application/xml; charset=utf-8');

echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n";
?>
<rss version="2.0" 
    xmlns:content="http://purl.org/rss/1.0/modules/content/"
    xmlns:wfw="http://wellformedweb.org/CommentAPI/"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:atom="http://www.w3.org/2005/Atom"
    xmlns:sy="http://purl.org/rss/1.0/modules/syndication/"
    xmlns:slash="http://purl.org/rss/1.0/modules/slash/">
    <channel>
        <title><?php bloginfo_rss('name'); ?></title>
        <atom:link href="<?php self_link(); ?>" rel="self" type="application/rss+xml" />
        <link><?php bloginfo_rss('url'); ?></link>
        <description><?php bloginfo_rss('description'); ?></description>
        <lastBuildDate><?php echo mysql2date('D, d M Y H:i:s +0000', get_lastpostmodified('GMT'), false); ?></lastBuildDate>
        <language><?php echo get_option('rss_language'); ?></language>
        <sy:updatePeriod>hourly</sy:updatePeriod>
        <sy:updateFrequency>1</sy:updateFrequency>
        <?php
        $args = array(
            'post_type' => 'post',
            'posts_per_page' => 50,
            'post_status' => 'publish'
        );
        $posts = new WP_Query($args);
        
        while ($posts->have_posts()) : $posts->the_post();
        ?>
        <item>
            <title><?php echo '<![CDATA[' . the_title_rss() . ']]>'; ?></title>
            <link><?php the_permalink_rss(); ?></link>
            <pubDate><?php echo mysql2date('D, d M Y H:i:s +0000', get_post_time('Y-m-d H:i:s', true), false); ?></pubDate>
            <dc:creator><![CDATA[<?php the_author(); ?>]]></dc:creator>
            <guid isPermaLink="false"><?php the_guid(); ?></guid>
            <description><![CDATA[<?php the_excerpt_rss(); ?>]]></description>
            <content:encoded><![CDATA[<?php
                $content = get_the_content_feed('rss2');
                // Get featured image
                if (has_post_thumbnail()) {
                    $image_url = get_the_post_thumbnail_url(null, 'full');
                    $content = '<img src="' . $image_url . '" />' . $content;
                }
                echo $content;
            ?>]]></content:encoded>
        </item>
        <?php endwhile; wp_reset_postdata(); ?>
    </channel>
</rss>
