COMPOSE = docker compose

.PHONY: init up test down
.DEFAULT_GOAL := help

# 初回セットアップまたは依存関係の更新時に実行
init:
	$(COMPOSE) build

# コンテナ起動
up:
	$(COMPOSE) up -d

# テスト実行
test:
	$(COMPOSE) run --rm app

# 後片付け
down:
	$(COMPOSE) down

# 使い方表示
help:
	@echo "make init  - ビルド（初回セットアップ）"
	@echo "make up    - コンテナ起動（バックグラウンド）"
	@echo "make test  - テスト実行（pytest）"
	@echo "make down  - コンテナ停止と後片付け"
