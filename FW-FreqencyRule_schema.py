{

    # mandatory 
    'alert_subject': {
        'required': True,
        'type': 'string'
    },
    'index': {
        'required': True,
        'type': 'string'
    },
    'type': {
        'required': True,
        'type': 'string'
    },
    # 'alert': {   It is not used in FW
    #     'required': True,
    #     'type': 'list'
    # },
#Mandatory Feilds for Frequency Rule Type
    'timeframe':{
        'required':True,
        'type': 'dict',
        'schema':{
            'minutes':{
                'required': False,
                'type':'number',
            },
            'hours':{
                'required': False,
                'type':'number',
            },
        },
    },
    'num_events': {
        'required': True,
        'type': 'number'
    },


# Optional
    'name':{
        'required': False,
        'type': 'string'
    },
    'use_strftime_index':{
        'required': False,
        'type': 'boolean'
    },

    'use_ssl':{
        'required': False,
        'type': 'boolean'
    },
    'verify_certs':{
        'required': False,
        'type': 'boolean'
    },
    'es_username':{
        'required': False,
        'type': 'string'
    },
    'es_password':{
        'required': False,
        'type': 'string'
    },
    'es_url_prefix':{
        'required': False,
        'type': 'string'
    },
    'es_send_get_body_as':{
        'required': False,
        'type': 'string'
    },
    'aggregation':{
        'required': False,
        'type': 'dict'
    },    
    'description':{
        'required': False,
        'type': 'string'
    },
    'generate_kibana_link':{
        'required': False,
        'type': 'boolean'
    },
    'use_kibana_dashboard':{
        'required': False,
        'type': 'string'
    },
    'kibana_url':{
        'required': False,
        'type': 'string'
    },
    'use_kibana4_dashboard':{
        'required': False,
        'type': 'string'
    },
    'kibana4_start_timedelta':{
        'required': False,
        'type': 'dict'
    },
    'kibana4_end_timedelta':{
        'required': False,
        'type': 'dict'
    },    
    'generate_kibana_discover_url':{
        'required': False,
        'type': 'boolean'
    },

    'kibana_discover_app_url':{
        'required': False,
        'type': 'string'
    },
    'kibana_discover_version':{
        'required': False,
        'type': 'string'
    },
    'kibana_discover_index_pattern_id':{
        'required': False,
        'type': 'string'
    },
    'kibana_discover_columns':{
        'required': False,
        'type': 'list'
    },

    'kibana_discover_from_timedelta':{
        'required': False,
        'type': 'dict'
    },        
    'kibana_discover_to_timedelta':{
        'required': False,
        'type': 'dict'
    },    

    'use_local_time':{
        'required': False,
        'type': 'boolean'
    },

    'realert':{
        'required': False,
        'type': 'dict',
        'schema':{
            'minutes':{
                'required': False,
                'type':'number',
            },
            'hours':{
                'required': False,
                'type':'number',
            },
        },
    }, 
    'exponential_realert':{
        'required': False,
        'type': 'dict'
    },    

    'match_enhancements':{
        'required': False,
        'type': 'list'
    },
    'top_count_number':{
        'required': False,
        'type': 'number'
    },
    'top_count_keys':{
        'required': False,
        'type': 'list'
    },
    'raw_count_keys':{
        'required': False,
        'type': 'boolean'
    },
    'include':{
        'required': False,
        'type': 'list'
    },

# This need to be check *********************####
    'filter':{
        'required': False,
        'type': 'list'
    },

    'max_query_size':{
        'required': False,
        'type': 'number'
    },
    'query_delay':{
        'required': False,
        'type': 'dict'
    },
    'owner':{
        'required': False,
        'type': 'string'
    },
    'priority':{
        'required': False,
        'type': 'number'
    },
    'category':{
        'required': False,
        'type': 'string'
    },
    'scan_entire_timeframe':{
        'required': False,
        'type': 'boolean'
    },
    'import':{
        'required': False,
        'type': 'string'
    },
    'buffer_time':{
        'required': False,
        'type': 'dict'
    },
    'timestamp_type':{
        'required': False,
        'type': 'string'
    },  
    'timestamp_format':{
        'required': False,
        'type': 'string'
    },  

    'timestamp_format_expr':{
        'required': False,
        'type': 'string'
    },
    '_source_enabled':{
        'required': False,
        'type': 'boolean'
    },
    'alert_text_args':{
        'required': False,
        'type': 'list'
    },
    #########Object need to be check
    # 'alert_text_kw':{
    #     'required': False,
    #     'type': 'object'
    # },
    'alert_missing_value':{
        'required': False,
        'type': 'string'
    },
    'is_enabled':{
        'required': False,
        'type': 'boolean'
    },
    'search_extra_index':{
        'required': False,
        'type': 'boolean'
    },

#########
    'alert_subject':{
        'required': False,
        'type': 'string'
    },
    'alert_subject_args':{
        'required': False,
        'type': 'list'
    },
  'email':{
        'required': False,
        'type': 'list'
    },
    'run_every':{
        'required': False,
        'type': 'dict'
    },

    #Optional Feilds for Frequency Rule type
    'query_key':{
        'required': False,
        'type': 'string'
    },
    'attach_related':{
        'required': False,
        'type': 'boolean'
    },
    'use_count_query':{
        'required': False,
        'type': 'boolean'
    },
    'doc_type':{
        'required': False,
        'type': 'string'
    },
    'use_terms_query':{
        'required': False,
        'type': 'boolean'
    },
    'terms_size':{
        'required': False,
        'type': 'number'
    },
    'forget_keys':{
        'required': False,
        'type': 'boolean'
    },

    #Aditional Feilds by FW
    'alerta_tags':{
        'required': False,
        'type': 'list'
    },
    'alerta_severity':{
        'required': False,
        'type': 'string'
    },
    'alerta_environment':{
        'required': False,
        'type': 'string'
    },
    'labels':{
        'required': False,
        'type': 'dict'
    },
}
