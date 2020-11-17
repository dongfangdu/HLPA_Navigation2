#!/bin/bash


( cd ./st_asr_optimization && tar -cvf dirs.tar src/ )
# ( cd ./st_audio_processing && tar -cvf dirs.tar src/ )
( cd ./st_case_recommendation && tar -cvf dirs.tar src/ cfg/ )
# ( cd ./st_element_extraction && tar -cvf dirs.tar src/ )
# ( cd ./st_knowledge_database && tar -cvf dirs.tar src/ )
( cd ./st_relation_extraction && tar -cvf dirs.tar src/ files/ images/ )
# ( cd ./st_semantic_understanding && tar -cvf dirs.tar src/ )
# ( cd ./st_smart_dialogue && tar -cvf dirs.tar src/ )
( cd ./st_text_classification && tar -cvf dirs.tar src/ )