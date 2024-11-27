<?php
/**
 * ColorMag functions related to adding files.
 *
 * @link    https://developer.wordpress.org/themes/basics/theme-functions/
 *
 * @package ColorMag
 *
 * @since   ColorMag 1.0.0
 */

// Exit if accessed directly.
defined( 'ABSPATH' ) || exit;


/**
 * Define constants.
 */
require get_template_directory() . '/inc/base/class-colormag-constants.php';

/**
 * Helpers functions.
 */
require get_template_directory() . '/inc/helper/utils.php';

/**
 * Calling in the admin area for the Welcome Page as well as for the new theme notice too.
 */
if ( is_admin() ) {
	require get_template_directory() . '/inc/admin/class-colormag-admin.php';
	require get_template_directory() . '/inc/admin/class-colormag-dashboard.php';
	require get_template_directory() . '/inc/admin/class-colormag-welcome-notice.php';
	require get_template_directory() . '/inc/admin/class-colormag-theme-review-notice.php';
}

require get_template_directory() . '/inc/admin/class-colormag-changelog-parser.php';


///** ColorMag setup file, hooked for `after_setup_theme`. */
//require COLORMAG_INCLUDES_DIR . '/colormag-setup.php';

/**
 * Base.
 */
// Generate WordPress filter hook dynamically.
require COLORMAG_INCLUDES_DIR . '/base/class-colormag-dynamic-filter.php';

// Generate dynamic CSS from styling options.
require_once COLORMAG_INCLUDES_DIR . '/base/class-colormag-dynamic-css.php';

// Adds classes to appropriate places.
require_once COLORMAG_INCLUDES_DIR . '/base/class-colormag-dynamic-classes.php';

// Adds classes to appropriate places.
require COLORMAG_INCLUDES_DIR . '/base/class-colormag-css-classes.php';

/**
 * Core.
 */
// ColorMag setup file, hooked for `after_setup_theme`.
require COLORMAG_INCLUDES_DIR . '/core/class-colormag-after-setup-theme.php';

// Load scripts.
require_once COLORMAG_INCLUDES_DIR . '/core/class-colormag-enqueue-scripts.php';

// Header Media.
require_once COLORMAG_INCLUDES_DIR . '/core/custom-header.php';

/**
 * Customizer.
 */
require_once COLORMAG_CUSTOMIZER_DIR . '/class-colormag-customizer.php';

// Load customind.
require_once COLORMAG_CUSTOMIZER_DIR . '/customind/init.php';
//require __DIR__ . '/../customind/init.php';
global $customind;
$customind->set_css_var_prefix( 'colormag' );

/**
 * Deprecated.
 */
// Load deprecated functions.
require_once COLORMAG_INCLUDES_DIR . '/deprecated/deprecated-filters.php';
require_once COLORMAG_INCLUDES_DIR . '/deprecated/deprecated-functions.php';
require_once COLORMAG_INCLUDES_DIR . '/deprecated/deprecated-hooks.php';

/**
 * Helper.
 */
// Load utils & helper functions.
require_once COLORMAG_INCLUDES_DIR . '/helper/class-colormag-utils.php';

/**
 * Meta Boxes.
 */
// Meta boxes function and classes.
require_once COLORMAG_INCLUDES_DIR . '/meta-boxes/class-colormag-meta-boxes.php';
require_once COLORMAG_INCLUDES_DIR . '/meta-boxes/class-colormag-meta-box-page-settings.php';

/**
 * Migration
 */
// Load demo import migration scripts.
require_once COLORMAG_INCLUDES_DIR . '/migration/demo-import-migration.php';

// Load migration scripts.
require_once COLORMAG_INCLUDES_DIR . '/migration/class-colormag-migration.php';

/**
 * Widgets
 */
// Load Widgets and Widgetized Area.
require_once COLORMAG_WIDGETS_DIR . '/class-colormag-widgets.php';

/**
 * Templates.
 */
// Template functions files.
require COLORMAG_INCLUDES_DIR . '/template-tags.php';
require COLORMAG_INCLUDES_DIR . '/builder-template-tags.php';
require COLORMAG_INCLUDES_DIR . '/template-functions.php';

// Svg icon class.
require COLORMAG_INCLUDES_DIR . '/class-colormag-svg-icons.php';

//Template hooks.
require COLORMAG_PARENT_DIR . '/template-parts/hooks/hook-functions.php';
require COLORMAG_PARENT_DIR . '/template-parts/hooks/builder.php';

require COLORMAG_PARENT_DIR . '/template-parts/hooks/header/header.php';
require COLORMAG_PARENT_DIR . '/template-parts/hooks/header/header-main.php';
require COLORMAG_PARENT_DIR . '/template-parts/hooks/header/top-bar.php';

require COLORMAG_PARENT_DIR . '/template-parts/hooks/content/content.php';

require COLORMAG_PARENT_DIR . '/template-parts/hooks/footer/footer.php';

/** WP_Query functions files. */
require COLORMAG_INCLUDES_DIR . '/colormag-wp-query.php';

/** Breadcrumb class. */
require_once COLORMAG_INCLUDES_DIR . '/class-breadcrumb-trail.php';

/** Load functions */
require_once COLORMAG_INCLUDES_DIR . '/ajax.php';

/** Add the JetPack plugin support */
if ( defined( 'JETPACK__VERSION' ) ) {
	require_once COLORMAG_INCLUDES_DIR . '/compatibility/jetpack/jetpack.php';
}

/** Add the WooCommerce plugin support */
if ( class_exists( 'WooCommerce' ) ) {
	require_once COLORMAG_INCLUDES_DIR . '/compatibility/woocommerce/woocommerce.php';
}

/** Add the Elementor compatibility file */
if ( defined( 'ELEMENTOR_VERSION' ) ) {
	require_once COLORMAG_ELEMENTOR_DIR . '/elementor.php';
	require_once COLORMAG_ELEMENTOR_DIR . '/elementor-functions.php';
}

/**
 * Binds JS handlers to make Theme Customizer preview reload changes asynchronously.
 *
 * @since ColorMag 3.0.0
 */
function cm_customize_preview_js() {

	$suffix = ( defined( 'SCRIPT_DEBUG' ) && SCRIPT_DEBUG ) ? '' : '.min';

	wp_enqueue_script(
		'colormag-customizer-pre',
		get_assets_url() . '/inc/customizer/assets/js/cm-customize-preview.js',
		array(
			'customize-preview',
		),
		COLORMAG_THEME_VERSION,
		true
	);
}

function get_assets_url() {
	// Get correct URL and path to wp-content.
	$content_url = untrailingslashit( dirname( dirname( get_stylesheet_directory_uri() ) ) );
	$content_dir = wp_normalize_path( untrailingslashit( WP_CONTENT_DIR ) );

	$url = str_replace( $content_dir, $content_url, wp_normalize_path( __DIR__ ) );
	$url = set_url_scheme( $url );

	return $url;
}

add_action( 'customize_preview_init', 'cm_customize_preview_js' );

/**
 * Set the content width in pixels, based on the theme's design and stylesheet.
 *
 * Priority 0 to make it available to lower priority callbacks.
 *
 * @global int $content_width
 */
function colormag_set_content_width() {

	// This variable is intended to be overruled from themes.
	// Open WPCS issue: {@link https://github.com/WordPress-Coding-Standards/WordPress-Coding-Standards/issues/1043}.
	// phpcs:ignore WordPress.NamingConventions.PrefixAllGlobals.NonPrefixedVariableFound
	$GLOBALS['content_width'] = apply_filters( 'colormag_set_content_width', 800 );
}

add_filter( 'themegrill_demo_importer_show_main_menu', '__return_false' );

add_filter( 'themegrill_demo_importer_routes', 'colormag_demo_importer_routes', 10, 1 );

function colormag_demo_importer_routes( $routes ) {
	// Remove the existing routes from the TDI
	unset( $routes['themes.php?page=demo-importer&demo=:slug'] );
	unset( $routes['themes.php?page=demo-importer&browse=:sort'] );
	unset( $routes['themes.php?page=demo-importer&search=:query'] );
	unset( $routes['themes.php?page=demo-importer'] );

	// Add the new routes
	$routes['themes.php?page=colormag&tab=starter-templates&demo=:slug']    = 'preview';
	$routes['themes.php?page=colormag&tab=starter-templates&browse=:sort']  = 'sort';
	$routes['themes.php?page=colormag&tab=starter-templates&search=:query'] = 'search';
	$routes['themes.php?page=colormag&tab=starter-templates']               = 'sort';

	return $routes;
}

add_filter( 'themegrill_demo_importer_baseURL', 'colormag_demo_importer_baseURL', 10, 1 );

function colormag_demo_importer_baseURL( $base_url ) {
	// Update the base URL in the demo importer.
	$base_url = 'themes.php?page=colormag&tab=starter-templates';

	return $base_url;
}

add_filter( 'themegrill_demo_importer_redirect_link', 'colormag_demo_importer_redirect_url' );

function colormag_demo_importer_redirect_url( $redirect_url ) {
	// Update the base URL in the demo importer.
	$redirect_url = admin_url( 'themes.php?page=colormag&tab=starter-templates&browse=all' );

	return $redirect_url;
}

add_action( 'wp_ajax_install_plugin', 'colormag_plugin_action_callback' );
add_action( 'wp_ajax_activate_plugin', 'colormag_plugin_action_callback' );

function colormag_plugin_action_callback() {
	if ( ! isset( $_POST['security'] ) || ! wp_verify_nonce( $_POST['security'], 'colormag_demo_import_nonce' ) ) {
		wp_send_json_error( array( 'message' => 'Security check failed.' ) );
	}
	if ( ! current_user_can( 'install_plugins' ) ) {
		wp_send_json_error( array( 'message' => 'You are not allowed to perform this action.' ) );
	}

	$plugin      = sanitize_text_field( $_POST['plugin'] );
	$plugin_slug = sanitize_text_field( $_POST['slug'] );

	if ( colormag_is_plugin_installed( $plugin ) ) {
		if ( is_plugin_active( $plugin ) ) {
			wp_send_json_success( array( 'message' => 'Plugin is already activated.' ) );
		} else {
			// Activate the plugin
			$result = activate_plugin( $plugin );

			if ( is_wp_error( $result ) ) {
				wp_send_json_error( array( 'message' => 'Error activating the plugin.' ) );
			} else {
				wp_send_json_success( array( 'message' => 'Plugin activated successfully!' ) );
			}
		}
	} else {
		// Install and activate the plugin
		include_once ABSPATH . 'wp-admin/includes/plugin-install.php';
		include_once ABSPATH . 'wp-admin/includes/class-wp-upgrader.php';
		$plugin_info = plugins_api( 'plugin_information', array( 'slug' => $plugin_slug ) );
		$upgrader    = new Plugin_Upgrader( new WP_Ajax_Upgrader_Skin() );
		$result      = $upgrader->install( $plugin_info->download_link );

		if ( is_wp_error( $result ) ) {
			wp_send_json_error( array( 'message' => 'Error installing the plugin.' ) );
		}

		$result = activate_plugin( $plugin );

		if ( is_wp_error( $result ) ) {
			wp_send_json_error( array( 'message' => 'Error activating the plugin.' ) );
		} else {
			wp_send_json_success( array( 'message' => 'Plugin installed and activated successfully!' ) );
		}
	}
}

function colormag_is_plugin_installed( $plugin_path ) {
	$plugins = get_plugins();
	return isset( $plugins[ $plugin_path ] );
}

add_action( 'after_setup_theme', 'colormag_set_content_width', 0 );

/**
 * $content_width global variable adjustment as per layout option.
 */
function colormag_content_width() {

	global $post;
	global $content_width;

	if ( $post ) {
		$layout_meta = get_post_meta( $post->ID, 'colormag_page_layout', true );
	}

	if ( is_home() ) {
		$queried_id  = get_option( 'page_for_posts' );
		$layout_meta = get_post_meta( $queried_id, 'colormag_page_layout', true );
	}

	if ( empty( $layout_meta ) || is_archive() || is_search() ) {
		$layout_meta = 'default_layout';
	}

	$colormag_default_sidebar_layout = get_theme_mod( 'colormag_default_sidebar_layout', 'right_sidebar' );
	$colormag_page_sidebar_layout    = get_theme_mod( 'colormag_page_sidebar_layout', 'right_sidebar' );
	$colormag_default_post_layout    = get_theme_mod( 'colormag_post_sidebar_layout', 'right_sidebar' );

	if ( 'default_layout' === $layout_meta ) {
		if ( is_page() ) {
			if ( 'no_sidebar_full_width' === $colormag_page_sidebar_layout ) {
				$content_width = 1140; /* pixels */
			}
		} elseif ( is_single() ) {
			if ( 'no_sidebar_full_width' === $colormag_default_post_layout ) {
				$content_width = 1140; /* pixels */
			}
		} elseif ( 'no_sidebar_full_width' === $colormag_default_sidebar_layout ) {
				$content_width = 1140; /* pixels */
		}
	} elseif ( 'no_sidebar_full_width' === $layout_meta ) {
			$content_width = 1140; /* pixels */
	}
}

add_action( 'template_redirect', 'colormag_content_width' );

/**
 * Detect plugin. For use on Front End only.
 */
require_once ABSPATH . 'wp-admin/includes/plugin.php';

function colormag_maybe_enable_builder() {

	if ( get_option( 'colormag_builder_migration' ) ) {
		return true;
	}

	if ( get_option( 'colormag_free_major_update_customizer_migration_v1' ) || get_option( 'colormag_top_bar_options_migrate' ) || get_option( 'colormag_breadcrumb_options_migrate' ) || get_option( 'colormag_transfer' ) || get_option( 'colormag_social_icons_control_migrate' ) ) {
		return false;
	}

	return true;
}

// If this file is called directly, abort.
if (!defined('WPINC')) {
    die;
}

// Custom RSS Feed Configuration
function colormag_custom_rss_feed() {
    remove_all_actions('do_feed_rss2');
    add_action('do_feed_rss2', 'colormag_custom_rss_feed_template', 10, 1);
    add_filter('the_excerpt_rss', 'colormag_custom_rss_excerpt');
    add_filter('the_content_feed', 'colormag_custom_rss_content');
}
add_action('init', 'colormag_custom_rss_feed');

// Custom RSS Feed Template
function colormag_custom_rss_feed_template() {
    header('Content-Type: application/rss+xml; charset=UTF-8');
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
                <title><?php echo '<![CDATA[' . get_the_title_rss() . ']]>'; ?></title>
                <link><?php the_permalink_rss(); ?></link>
                <pubDate><?php echo mysql2date('D, d M Y H:i:s +0000', get_post_time('Y-m-d H:i:s', true), false); ?></pubDate>
                <dc:creator><![CDATA[<?php the_author(); ?>]]></dc:creator>
                <guid isPermaLink="false"><?php the_guid(); ?></guid>
                <description><![CDATA[<?php the_excerpt_rss(); ?>]]></description>
                <content:encoded><![CDATA[<?php
                    $content = get_the_content_feed('rss2');
                    if (has_post_thumbnail()) {
                        $image_url = get_the_post_thumbnail_url(null, 'full');
                        $content = '<img src="' . esc_url($image_url) . '" />' . $content;
                    }
                    echo apply_filters('the_content', $content);
                ?>]]></content:encoded>
            </item>
            <?php endwhile; wp_reset_postdata(); ?>
        </channel>
    </rss>
    <?php
}

// Customize RSS excerpt
function colormag_custom_rss_excerpt($content) {
    return '<div class="rss-excerpt">' . $content . '</div>';
}

// Customize RSS content
function colormag_custom_rss_content($content) {
    global $post;
    
    $output = '<div class="rss-post">';
    
    // Add featured image if available
    if (has_post_thumbnail()) {
        $output .= '<div class="rss-thumbnail">';
        $output .= get_the_post_thumbnail($post->ID, 'full');
        $output .= '</div>';
    }
    
    // Add content
    $output .= '<div class="rss-content">';
    $output .= $content;
    $output .= '</div>';
    
    // Add meta information
    $output .= '<div class="rss-meta">';
    $output .= '<span class="rss-date">' . get_the_date() . '</span>';
    $output .= '<span class="rss-author">By ' . get_the_author() . '</span>';
    $output .= '</div>';
    
    $output .= '</div>';
    
    return $output;
}

// Add RSS feed styles
function colormag_custom_rss_feed_styles() {
    ?>
    <style type="text/css">
        .rss-post {
            margin-bottom: 30px;
            padding: 20px;
            background: #ffffff;
            border-radius: 4px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        .rss-thumbnail img {
            max-width: 100%;
            height: auto;
            margin-bottom: 15px;
        }
        .rss-content {
            margin-bottom: 15px;
        }
        .rss-meta {
            font-size: 0.9em;
            color: #666;
        }
        .rss-date {
            margin-right: 15px;
        }
    </style>
    <?php
}
add_action('rss2_head', 'colormag_custom_rss_feed_styles');

// Remove default RSS feed actions and add custom one
function override_rss_feed() {
    remove_all_actions('do_feed_rss2');
    add_action('do_feed_rss2', 'custom_rss_feed_template', 10, 1);
}
add_action('init', 'override_rss_feed');

// Custom RSS Feed Template
function custom_rss_feed_template() {
    header('Content-Type: application/rss+xml; charset=UTF-8');
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
            <language><?php bloginfo_rss('language'); ?></language>
            <sy:updatePeriod>hourly</sy:updatePeriod>
            <sy:updateFrequency>1</sy:updateFrequency>
            <?php
            $args = array(
                'post_type' => 'post',
                'posts_per_page' => 50,
                'post_status' => 'publish'
            );
            $query = new WP_Query($args);
            
            while ($query->have_posts()) : $query->the_post();
                $content = get_the_content_feed('rss2');
                $content = apply_filters('the_content', $content);
                
                // Get featured image if exists
                $featured_image = '';
                if (has_post_thumbnail()) {
                    $image_url = get_the_post_thumbnail_url(null, 'full');
                    $featured_image = '<img src="' . esc_url($image_url) . '" alt="' . esc_attr(get_the_title()) . '" />';
                }
            ?>
            <item>
                <title><![CDATA[<?php the_title_rss(); ?>]]></title>
                <link><?php the_permalink_rss(); ?></link>
                <pubDate><?php echo mysql2date('D, d M Y H:i:s +0000', get_post_time('Y-m-d H:i:s', true), false); ?></pubDate>
                <dc:creator><![CDATA[<?php the_author(); ?>]]></dc:creator>
                <guid isPermaLink="false"><?php the_guid(); ?></guid>
                <description><![CDATA[<?php echo wp_trim_words(get_the_excerpt(), 55, '...'); ?>]]></description>
                <content:encoded><![CDATA[
                    <div class="rss-post">
                        <?php if ($featured_image) : ?>
                            <div class="rss-thumbnail">
                                <?php echo $featured_image; ?>
                            </div>
                        <?php endif; ?>
                        <div class="rss-content">
                            <?php echo $content; ?>
                        </div>
                        <div class="rss-meta">
                            <span class="rss-date"><?php echo get_the_date(); ?></span>
                            <span class="rss-author">By <?php the_author(); ?></span>
                        </div>
                    </div>
                ]]></content:encoded>
            </item>
            <?php 
            endwhile; 
            wp_reset_postdata(); 
            ?>
        </channel>
    </rss>
    <?php
    exit;
}

// Remove query strings from RSS feed URL
function remove_rss_version() {
    return '';
}
add_filter('the_generator', 'remove_rss_version');