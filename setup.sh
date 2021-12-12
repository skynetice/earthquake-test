mkdir -p ~/.streamlit/

echo "\
[server]\nheadless = true\nenableCORS=false\nport = \n
" > ~/.streamlit/config.toml
