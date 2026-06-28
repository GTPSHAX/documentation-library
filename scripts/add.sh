#!/usr/bin/env bash

set -e

CONFIG_FILE="sources.txt"

if [ ! -f "$CONFIG_FILE" ]; then
  echo "Configuration file not found: $CONFIG_FILE"
  exit 1
fi

while IFS="|" read -r NAME REPO REF SPARSE_PATH MODE; do
  # Skip comments and empty lines
  [[ -z "$NAME" || "$NAME" =~ ^# ]] && continue

  echo "----------------------------------------"
  echo "Repository : $NAME"
  echo "Reference  : $REF"
  echo "Path       : $SPARSE_PATH"
  echo "Mode       : $MODE"
  echo "----------------------------------------"

  if [ ! -d "$NAME" ]; then
    echo "Cloning repository..."

    git clone \
      --depth=1 \
      --filter=blob:none \
      --sparse \
      --branch="$REF" \
      "$REPO" \
      "$NAME"

    cd "$NAME"

    echo "Configuring sparse checkout..."
    git sparse-checkout set "$SPARSE_PATH"

    if [ "$MODE" = "archive" ]; then
      echo "Removing Git metadata..."
      rm -rf .git
    fi

    cd ..
    echo "Completed."
  else
    if [ "$MODE" = "archive" ]; then
      echo "Archive already exists."
      echo "Delete the directory manually if you want to re-sync."
    else
      if [ -d "$NAME/.git" ]; then
        echo "Updating repository..."

        cd "$NAME"

        git fetch --depth=1 origin "$REF"
        git checkout "$REF"
        git sparse-checkout set "$SPARSE_PATH"

        git pull origin "$REF" || true

        cd ..

        echo "Completed."
      else
        echo "Directory exists but is not a Git repository."
        echo "Skipping."
      fi
    fi
  fi
done < "$CONFIG_FILE"

echo "Synchronization completed."
