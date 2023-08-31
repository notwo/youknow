import { ref, reactive, readonly } from "vue";

export function useStore() {
  const items = reactive({ list: [] });
  let backupList = [];

  function setItem<T>(list: T[]) {
    items.list = ref(list);
    backupList = list.concat();
  }

  function add<T>(item: T) {
    items.list.unshift(item);
    backupList.unshift(item);
  }

  function remove(id: Number) {
    let _target = items.list.filter(obj => obj.id === id);
    let _removeIndex = items.list.indexOf(_target[0]);
    items.list.splice(_removeIndex, 1);

    _target = backupList.filter(obj => obj.id === id);
    _removeIndex = backupList.indexOf(_target[0]);
    backupList.splice(_removeIndex, 1);
  }

  function search<T>(list: T[]) {
    restore();
    list.map((obj: object) => {
      const _target = items.list.filter(_item => _item.id !== obj.id);
      _target.map((_deleteTarget: Object) => {
        const _removeIndex = items.list.indexOf(_deleteTarget);
        items.list.splice(_removeIndex, 1);
      });
    });
  }

  function restore() {
    if (items.list.length === backupList.length) { return; }

    const length = items.list.length;
    backupList.map((obj: Object) => {
      items.list.push(obj);
    });
    for(let _i = 0;_i < length;_i++) {
      items.list.shift();
    }
  }

  function allClear() {
    items.list.splice(0);
  }

  return { items: readonly(items), setItem, add, remove, search, restore, allClear };
};
