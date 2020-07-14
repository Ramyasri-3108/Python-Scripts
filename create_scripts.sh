#!/bin/bash
read -p "Enter the name of script: " name
`touch $name`
echo "#!/bin/bash" > $name
`chmod +x $name`

