#!/usr/bin/env bash

irc_setenv_mode=${1:-build}

here="$(pwd -P)"
lib_dir="$here/"

prepare_environment() (
	set -e

	if [ "$irc_setenv_mode" = "rebuild" ]; then
		echo
		echo "Removing environment..."
		rm -rf ".env"
	fi

	if [ ! -d ".env" ]
	then
		echo
		echo "Creating environment..."
		python3 -m venv .env
		source .env/bin/activate

		echo "Installing requirements..."
		pip3 install --upgrade pip
		pip3 install -r "$here/requirements.txt"
	fi
)

activate_environment() {
	echo "Activating environment..."
	source .env/bin/activate
}

prepare_environment &&
	activate_environment &&
	export PYTHONPATH="$lib_dir" &&
	export PYTHONIOENCODING=utf8
