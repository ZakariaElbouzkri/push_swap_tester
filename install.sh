curent_dir=$(pwd)
command_dir="python3 $curent_dir/main.py"
echo "alias ps_tester=\"$command_dir"\" >> ~/.zshrc 
echo "alias ps_tester=\"$command_dir"\" >> ~/.bashrc

echo "\033[92m" "Installed, usage:" "\033[0m"
echo "\tps_tester numberOfTestCase StackSize star end" "\033[0m"

