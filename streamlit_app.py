import streamlit as st
import clips
import logging

# setup working environment
logging.basicConfig(level=15, format='%(message)s')

env = clips.Environment()
router = clips.LoggingRouter()
env.add_router(router)

# input
name = st.text_input("Enter your name")

# knwoledge base
env.build('(deftemplate result (slot name))')
env.assert_string(f'(result (name "{name}"))')
# inference
env.run()

# output
results = []
for fact in env.facts():
    if fact.template.name == 'result':
        results.append(fact['name'])

        st.write(results[0], "better output")
