import { reactive, readonly } from "vue";

export function useStore() {
  const items = reactive({ list: [] });

  function setItem<T>(list: T[]) {
    items.list = list;
  }

  function add<T>(item: T) {
    items.list.unshift(item);
  };

  function remove(id: Number) {
    const _target = items.list.filter(obj => obj.id === id);
    const _removeIndex = items.list.indexOf(_target[0]);
    items.list.splice(_removeIndex, 1);
  }

  return { items: readonly(items), add, setItem, remove };
};
