<?php

// place this code into the functions.php file from your child theme


// Show date info on a single event page
add_shortcode('fw_eo_date_time', function($atts) {
	$atts = shortcode_atts( array(
		'timelabel' => __('Time', 'eventorganiser'),
		'to' => '-',
		'prefix' => ''
	), $atts, 'fw_eo_date_time' );
	$html = '';
	if ( eo_recurs() ) {
		$occurrence_id = (!empty($_GET['occurrence'])) ? (int)$_GET['occurrence'] : false;
		$start_date = eo_get_the_start('j M Y', get_the_ID(), $occurrence_id);
		if ( $start_date ) {
			$html .= '<p><strong>'.__( 'Date', 'eventorganiser' ).':</strong> '.$start_date;
			if (!eo_is_all_day()) $html .= '<br><strong>'.$atts['timelabel'].':</strong> '.eo_get_the_start('H:i').' '.$atts['to'].' '.eo_get_the_end('H:i').' '.$atts['prefix'];
			$html .= '<br><em>' . __( 'This event will repeat', 'eventorganiser' ).'.</em></p>';
		} else {
			$html = sprintf( '<p>' . __( 'This event finished on %s', 'eventorganiser' ) . '</p>', eo_get_schedule_last( 'd M Y', '' ) );
		}
	} else {
		$start_date = eo_get_the_start('j M Y');
		$html = '<p><strong>'.__( 'Date', 'eventorganiser' ).':</strong> '.$start_date;
		$end_date = eo_get_the_end('j M Y');
		if ($start_date != $end_date) $html .= ' - '.$end_date;
		if (!eo_is_all_day()) $html .= '<br><strong>'.$atts['timelabel'].':</strong> '.eo_get_the_start('H:i').' '.$atts['to'].' '.eo_get_the_end('H:i').' '.$atts['prefix'].'</p>';
	}
	return $html;
});

// show the event date in the loop (for example)
add_shortcode('fw_eo_simple_date', function($atts) {
	$atts = shortcode_atts( array(
		'expired' => ''
	), $atts, 'fw_eo_simple_date' );
	$html = '';
	$start_date = eo_get_the_start('j M Y');
	if ( $start_date ) {
		$html = '<p class="event-date">'.__( 'Date', 'eventorganiser' ).': '.$start_date;
		$end_date = eo_get_the_end('j M Y');
		if ($start_date != $end_date) $html .= ' - '.$end_date; // multiple day event
		$html .= '</p>';
	} else {
		$html = '<p class="event-date">'.$atts['expired'].'</p>';
	}
	return $html;
});

// Show event venue information 
add_shortcode('fw_eo_venue', function() {
	$html = '';
	if ( eo_get_venue() ) {
		$tax = get_taxonomy( 'event-venue' );
		$html = '<p><strong>'.__( $tax->labels->singular_name ).':</strong> <a href="'.eo_get_venue_link().'"> '.eo_get_venue_name().'</a>';
		$adres = eo_get_venue_address();
		if ($adres['address'] != '' && $adres['city'] != '') {
			$html .= '<br><strong>'.__( 'Address', 'eventorganiser' ).':</strong> '.$adres['address'].', ';
			if ($adres['postcode'] != '') $html .= $adres['postcode'].' ';
			$html .= $adres['city'];
		}
		$html .= '</p>';
	}
	return $html;
});

// Creates the link to the event detail page
add_shortcode('fw_eo_detail_url', function($atts) {
	return get_permalink().'?occurrence='.eo_get_the_occurrence_id(); 
});

?>