#!/bin/bash

while true; do
    clear
    echo "----- Menu -----"
    echo "1. Start development server"
    echo "2. Build documentation"
    echo "3. Deploy documentation to GitHub Pages"
    echo "4. Exit"

    read -p "Enter your choice (1-4): " choice
    echo

    case $choice in
        1)
            echo "Starting development server..."
            docker run --rm -it -p 8000:8000 -v ${PWD}:/docs squidfunk/mkdocs-material
            ;;
        2)
            echo "Building documentation..."
            docker run --rm -it -v ${PWD}:/docs squidfunk/mkdocs-material build
            ;;
        3)
            echo "Deploying documentation to GitHub Pages..."
            docker run --rm -it -v ~/.ssh:/root/.ssh -v ${PWD}:/docs squidfunk/mkdocs-material gh-deploy
            ;;
        4)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid choice. Please enter a number between 1 and 4."
            ;;
    esac

    read -rp "Press Enter to continue..."
done
